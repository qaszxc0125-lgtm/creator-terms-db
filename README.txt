Creator Terms DB — 31-record prototype

Contents
- index.html: standalone searchable database page (31 records)
- database.json: structured data for future updates
- scripts/validate_database.py: checks count, duplicate names, and HTML/JSON synchronization
- .github/workflows/pages.yml: validates and deploys the site to GitHub Pages on pushes to main; includes a weekly scheduled validation/deploy run

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
