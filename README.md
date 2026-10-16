# THE SIR FILES

Independent documentary investigation of India’s Special Intensive Revision of electoral rolls.

## Scope

48 addressable HTML pages, 36 State/UT files, 8 developed local analyses and 28 reference files. Dated review, legal analysis, chronology, national reconciliation, source ledger, claims register and proposed ECINet audit. Review date: 17 October 2026 IST. Sources checked through 16 October.

This is an initial research edition. It is not a completed national forensic audit, voter-registration service, live ECI integration or scheduled autonomous investigation.

## Publish with GitHub Pages

Repository Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save.

Live URL, verified 17 October 2026 IST: https://ashish-bhatia.github.io/the-sir-files/

The site is buildless and contains .nojekyll. No custom GitHub Actions workflow, API keys, packages or server is needed. GitHub may run its own Pages deployment infrastructure after branch publishing is enabled.

## Verify

Run `python3 scripts/validate.py` and `node --check assets/site.js`.

Serve locally with `python3 -m http.server 8080`. Relative paths support the project subdirectory used by GitHub Pages. Search, state filters, source filters, claim filtering and data downloads use local static assets.

## Evidence and corrections

`assets/research-data.json` contains sources with per-source review status, jurisdiction records, chronology, questions, corrections and claims. `assets/claims.csv` exports the claims register. New reports identify primary evidence, official positions, secondary reporting, analytical proposals and remaining gaps. Prior Tripura correction retained. Form 7 source gap closed in this edition.

The source archive from the earlier edition was restored from the existing project deliverable, then revised. Older local narratives remain subject to their disclosed evidence limitations. Remote sources are linked, not mirrored. Personal voter documents are not hosted.
