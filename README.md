# THE SIR FILES

Independent documentary investigation of India’s Special Intensive Revision of electoral rolls.

## Scope

64 research/navigation pages plus a 404 page, 36 State/UT files, 8 developed local analyses and 28 reference files. Dated review, legal analysis, chronology, national reconciliation, source ledger, claims register and proposed ECINet audit. Review date: 17 October 2026 IST. Latest source review: 17 October. Earlier records retain their own review status.

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

## Continuation review, edition 1.1

Added signed Maharashtra extension and CEO application bulletin, public timetable inconsistency analysis, an SSR revision-stage map and five new tracked claims. 36 source records and 17 claims. Original October 1 ECI drive order now directly inspected. Gazette publication and outcome reconciliation remain open.

## Full audit, edition 1.2

52 research/navigation pages, 41 source records, 20 claims and a 14-topic gap register. All 36 jurisdiction files are data-backed; 8 remain developed analyses and 28 remain reference files. Source records include aliases, mirrors and an explicitly unverified Delhi retrieval lead, so they are not independent corroboration counts.

Added a 13-district Uttarakhand reconciliation CSV, standard Form 6 analysis and full coverage audit. Narrowed the historical Uttarakhand date anomaly, added later Tripura reporting, refreshed West Bengal orders and flagged the historical Act compilation. No independent person-level legality audit is claimed.

After changing `assets/research-data.json`, run `python3 scripts/render_research.py` then `python3 scripts/validate.py`. The renderer synchronises state files, source and claim registers, gap register, chronology, search and sitemap.

## Follow-up and editorial edition 1.3

- Two new research notes: the 14 October Delhi High Court Form 6 order and the ECI statutory compilation dated July 2025.
- 44 source records and 23 tracked claims. Delhi re-verification reporting remains distinct from signed instructions and completed restorations.
- The Delhi order is a publisher-hosted copy, with identical bytes from a second publisher. Court-portal and cryptographic-signature checks are not claimed.
- The newer Act compilation is dated July 2025. Later legal changes and current rule versions remain an open check.
- Editorial masthead, lead report, edition notes, source-based Goa stock comparison, searchable state files and article contents menus. Light and dark themes use independently loaded, content-addressed assets.
- Run `python3 scripts/validate_cases.py` and `node scripts/ui-smoke.cjs` for structure and browser-local logic checks. These do not replace rendered browser inspection.

## Case-led reading structure

The publication uses one fixed light editorial palette. It ignores system dark mode and previous theme preferences. Theme controls and the old theme script have been removed.

`assets/case-studies.json` defines four thematic groups, eight documentary case overviews and 17 supporting chapters. Each overview gives the question, the sequence of events, established evidence, limits, missing records and an ordered reading path. Supporting articles link back to the case and forward to the next chapter.

The homepage and case hub introduce the groups. `start-here/` explains the process and reading method. The state directory opens developed cases at their overview and keeps the 28 reference files clearly labelled. The research page records updates within their case context.

Run `python3 scripts/render_research.py`, `python3 scripts/validate.py`, `python3 scripts/validate_cases.py` and `node scripts/ui-smoke.cjs`. Rendering remains idempotent. The research dataset and evidence status are unchanged by this structural edition.
