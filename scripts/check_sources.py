#!/usr/bin/env python3
"""Monitor official source pages for changes; flag review, never rewrite factual claims automatically."""
import concurrent.futures, hashlib, json, os, re, urllib.error, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH, STATE_PATH = ROOT / "database.json", ROOT / "source-check-state.json"
REPORT_PATH, SUMMARY_PATH = ROOT / "source-check-report.md", ROOT / "source-check-summary.json"
MAX_BYTES = 2_000_000
USER_AGENT = "CreatorTermsDBSourceMonitor/1.0 (+https://github.com/qaszxc0125-lgtm/creator-terms-db)"

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.title_parts, self.in_title, self.skip_depth = [], [], False, 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg", "template"): self.skip_depth += 1
        if tag == "title": self.in_title = True
    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg", "template") and self.skip_depth: self.skip_depth -= 1
        if tag == "title": self.in_title = False
    def handle_data(self, data):
        value = re.sub(r"\s+", " ", data).strip()
        if value:
            if self.in_title: self.title_parts.append(value)
            if not self.skip_depth: self.parts.append(value)

def fetch_source(entry):
    url = entry.get("url", "")
    result = {"name": entry.get("name", "(unnamed)"), "url": url, "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "http_status": None, "title": "", "content_sha256": "", "error": ""}
    if not url.startswith(("https://", "http://")):
        result["error"] = "URL is missing or is not HTTP(S)"
        return result
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            result["http_status"] = response.getcode()
            content_type = response.headers.get("Content-Type", "")
            body = response.read(MAX_BYTES)
        found = re.search(r"charset=([^\s;]+)", content_type, re.I)
        charset = found.group(1).strip("\"'") if found else "utf-8"
        parser = TextExtractor()
        parser.feed(body.decode(charset, errors="replace"))
        normalized = re.sub(r"\s+", " ", " ".join(parser.parts)).strip()
        result["title"] = " ".join(parser.title_parts)[:300]
        result["content_sha256"] = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        if result["http_status"] >= 400: result["error"] = "HTTP status " + str(result["http_status"])
        elif not normalized: result["error"] = "Page returned no extractable text (may be JavaScript-rendered or blocked)"
    except urllib.error.HTTPError as exc:
        result["http_status"], result["error"] = exc.code, "HTTP status " + str(exc.code)
    except Exception as exc:
        result["error"] = type(exc).__name__ + ": " + str(exc)[:250]
    return result

def main():
    data = json.loads(DB_PATH.read_text(encoding="utf-8"))
    try: old = json.loads(STATE_PATH.read_text(encoding="utf-8")).get("sources", {}) if STATE_PATH.exists() else {}
    except Exception: old = {}
    unique = {}
    for entry in data.get("entries", []):
        if entry.get("url"): unique.setdefault(entry["url"], entry)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch_source, unique.values()))
    results.sort(key=lambda item: item["name"].casefold())
    changed, errors, next_sources = [], [], {}
    for item in results:
        previous = old.get(item["url"])
        if item["error"]: errors.append(item)
        if previous:
            diffs = [label + " changed" for field, label in (("http_status", "HTTP status"), ("title", "page title"), ("content_sha256", "page text")) if item.get(field) != previous.get(field)]
            if diffs: item["change"] = ", ".join(diffs); changed.append(item)
        elif item["error"]:
            item["change"] = "Initial check failed"; changed.append(item)
        next_sources[item["url"]] = item
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    STATE_PATH.write_text(json.dumps({"checked_at": now, "source_count": len(results), "sources": next_sources}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    alert = bool(changed or errors)
    lines = ["# Creator Terms DB — official source check", "", "- Checked at (UTC): " + now, "- Unique source URLs checked: " + str(len(results)), "- Changed sources: " + str(len(changed)), "- Sources needing attention: " + str(len(errors)), "", "This monitor detects source-page changes and access failures. It does not automatically alter commercial-use, free-tier, or affiliate claims; review the official page before updating database records.", ""]
    if changed:
        lines += ["## Changed or newly failing sources", ""]
        for item in changed:
            lines += ["### " + item["name"], "- URL: " + item["url"], "- Change: " + item.get("change", "Needs review"), "- HTTP status: " + str(item.get("http_status")), "- Page title: " + (item.get("title") or "(not detected)"), "- Error: " + (item.get("error") or "None"), ""]
    if errors:
        lines += ["## Access or extraction errors", ""]
        for item in errors: lines.append("- **" + item["name"] + "** — " + item["url"] + " — " + item["error"])
        lines.append("")
    if not alert: lines += ["## Result", "", "No source text changes or access errors detected against the previous baseline."]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    SUMMARY_PATH.write_text(json.dumps({"alert": alert, "changed_count": len(changed), "error_count": len(errors), "source_count": len(results), "checked_at": now}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Checked", len(results), "unique URLs;", len(changed), "changed;", len(errors), "errors.")
    with open(os.environ.get("GITHUB_OUTPUT", "/dev/null"), "a", encoding="utf-8") as output:
        output.write("alert=" + ("true" if alert else "false") + "\n")
        output.write("changed_count=" + str(len(changed)) + "\n")
        output.write("error_count=" + str(len(errors)) + "\n")

if __name__ == "__main__": main()
