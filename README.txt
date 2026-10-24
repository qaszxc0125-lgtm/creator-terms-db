Creator Terms DB — 31-record prototype

Contents
- index.html: standalone searchable database page (31 records)
- ai-commercial-use-guide.html: SEO-oriented guide comparing free-tier commercial-use conditions
- ai-stock-submission-guide.html: SEO guide comparing Adobe Stock and Shutterstock AI submission rules
- database.json: structured data for future updates
- scripts/validate_database.py: checks count, duplicate names, and HTML/JSON synchronization
- .github/workflows/pages.yml: validates and deploys the site to GitHub Pages when relevant site files change on main; article HTML changes now trigger deployment too.
- sitemap.xml: lists the six public pages for search engines.
- editorial-policy.html: explains editorial/update practices, affiliate disclosure approach, privacy notes, and disclaimers.
- robots.txt: allows standard crawling and points crawlers to the sitemap.

Quality notes (checked 2026-10-24)
- Microsoft Designer: Microsoft Support FAQ describes use as personal/non-commercial; not recommended for commercial projects.
- Pika: official support and pricing page show a possible mismatch about which paid plans include commercial rights; verify the exact plan before commercial use.
- Canva AI: official Japanese page describes free-plan image-generation limits; these can change and should be rechecked.
- Gemini image generation: commercial terms remain unverified in this dataset.
- Adobe Firefly affiliate program: official Japanese page is currently a waitlist, not an open formal application.
- Leonardo.Ai affiliate program: official help says the program closed on April 7, 2026.
- Canva affiliate benefits: official Canvassador route only, currently closed to new applications.
- OpenArt: official affiliate application page exists; approval is required.

Current limitations
- Static site; no backend, analytics, or affiliate tracking.
- Many free-plan quotas and affiliate availability are still unverified.
- The workflow automates validation and deployment only; it does not automatically verify changing provider terms or update the records.
- GitHub Pages must be enabled for the repository with the source set to GitHub Actions. The first setup may require a one-time setting in the repository's Settings > Pages.
- Official terms can change. Re-check source terms before use and before publishing commercial content.
- This is an information aid, not legal advice.

Zero-cost deployment
1. Create a GitHub repository named creator-terms-db (public is easiest for a public website).
2. Upload the contents of this folder to the repository root, including the hidden .github folder.
3. In repository Settings > Pages, set the build/deployment source to GitHub Actions if it is not already set.
4. Push to the main branch or run the workflow manually under Actions. After a successful run, GitHub Pages will show the public URL.

2026-10-24 品質更新
- Ideogram：公式料金ページに基づき、無料アカウントの週次クレジット（量は変動）、画像の既定公開、商用利用案内を反映。
- Krea：公式料金ページに基づき、Freeの100 units/日と商用ライセンス表記を反映。Creator Programは応募・審査制として区別。
- Recraft：Freeの最大30クレジット/日、無料生成物の公開・商用利用不可、生成時点のプランが権利を決める点を反映。
- HTML埋め込みデータとdatabase.jsonを同期し、紹介報酬に関するフッター表記を更新。
- GitHub Pages用ワークフローと、HTML/JSON同期検証スクリプトを追加。


## Automatic official-source monitoring
- `scripts/check_sources.py` checks the official URLs in `database.json` weekly, records HTTP status/title/normalized page-text fingerprints, and compares them with the prior baseline.
- `scripts/test_check_sources.py` tests source-error classification; the monitor workflow runs Python syntax validation and unit tests before checking URLs.
- Access failures are classified to distinguish likely broken URLs (404/410), access restrictions or rate limits (401/403/407/429), temporary server failures (5xx), and network/client errors. A 403 is not treated as proof that a URL is dead.
- If a source changes or cannot be accessed, the workflow creates or updates a GitHub Issue for review and stores a downloadable report artifact.
- This is change detection, not automated legal interpretation: the monitor never rewrites commercial-use, free-tier, or affiliate claims by itself. Review the official source and then update `database.json` and `index.html` together.
- Workflow: `.github/workflows/source-monitor.yml`. Run it manually from the Actions tab when needed.


2026-10-24 official-source review
- Kling AI: official Terms of Service §4.6 conflicts with official FAQ/promotional claims about free-tier commercial use. The database now marks this as unresolved and recommends written confirmation before commercial use of free outputs.
- Krea: official pricing page confirms Free 100 units/day and a commercial license; the Creator Program is application/selection-based and may include affiliate rewards.


2026-10-24 source-link maintenance
- ChatGPT: source link now points to OpenAI Help Center's explicit commercial-use FAQ, which states that outputs may be sold/reused subject to Terms and Content Policy.
- Canva AI: source link now points to Canva's Japanese AI page with a direct commercial-use explanation; exact AI limits are treated as variable rather than a fixed guaranteed quota.

- ai-tool-affiliate-programs.html: official-source comparison of AI tool affiliate/creator programs, eligibility and current application status
- ai-tool-affiliate-start-guide.html: beginner guide covering content preparation, application checks, disclosure, and measurement for AI-tool affiliate marketing

2026-10-24 affiliate program review
- Runway: official affiliate page lists $15 per new paid subscriber, a 25% discount code for referred users, and an application/review process. Bank-country payment eligibility should be confirmed during application.
- Krea: creator program is selective; affiliate rewards are possible, but exact reward details vary.
- Canva: official help says affiliate benefits are only through Canvassador; new applications are currently closed.
- Kling AI: official affiliate page exists, but public pages do not establish a definitive commission rate or Japan eligibility. Referral-credit benefits are distinguished from cash affiliate rewards.
- Adobe Firefly: prior review found a waitlist-stage affiliate program; do not count it as active until public application terms are confirmed.

- gemini-image-commercial-use.html: official-source guide explaining that Gemini Apps image-use terms do not establish blanket commercial/stock licensing; links to Google Help, GenAI policy, and API terms.

2026-10-24 Gemini source review
- Gemini Apps official help: use is subject to Google Terms and Prohibited Use Policy; users should avoid third-party copyright/privacy violations and exercise judgment before publishing or using generated content. Work/school accounts may have different terms.
- The database keeps Google Gemini image generation as `commercial: unknown` because the cited official help does not expressly establish blanket permission for all commercial or stock-sale uses. API users should separately review Gemini API terms.


2026-10-24 affiliate onboarding guide
- Added a beginner-focused article explaining how to prepare useful content, verify official program terms, disclose affiliate relationships, and measure results.
- Linked the new guide from the homepage and the affiliate-program comparison page, and added it to sitemap.xml.
- No affiliate tracking links, analytics tags, or claims of program approval were added.
