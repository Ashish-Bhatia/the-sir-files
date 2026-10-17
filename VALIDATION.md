# Publication validation, 17 October 2026 IST

## Passed

- 52 research/navigation pages plus one 404 page.
- Internal page, asset and fragment checks: zero missing targets.
- One title per HTML page; no duplicate element IDs.
- 36 jurisdiction records; source references resolve in the 41-record ledger.
- All 20 claims link to existing sources. CSV and JSON row counts agree.
- Goa draft-to-final equation, pre-to-draft count and logical-discrepancy category sum reconcile.
- Node syntax checks pass for site.js and search-data.js.

## Verification limits

- No rendered browser QA performed in this environment. Mobile layout and interactions still need a browser inspection.
- CSS parser unavailable; no new parser result claimed.
- External links have per-source review status. Carried-forward sources have not all been independently reauthenticated.
- No internal ECINet access, person-level roll audit, original approval minutes, authenticated October Form 6 court order or national wrongful-exclusion total obtained.
- No RTI requests, institutional enquiries or submissions sent.
- Repository publication and GitHub Pages deployment are distinct. A repository commit is not evidence that Pages hosting has been enabled.

## Reproduce

Run `python3 scripts/validate.py`, `node --check assets/site.js` and `node --check assets/search-data.js` from the repository root.

## Prior edition live deployment verification

GitHub Pages returned HTTP 200 for the homepage, research, Form 7, ECINet, claims register, research JSON and site JavaScript. All seven responses matched the committed local files byte for byte. Live JSON contained 31 sources, 12 claims and 36 jurisdictions. Verified 17 October 2026 IST. This verifies serving and edition identity, not rendered browser behaviour.

## Edition 1.1 continuation checks

- Added two research articles, five sources and five claims.
- The 17 scheduled, 16 deferred and 3 not-started jurisdiction groups are disjoint and cover all 36 records.
- Maharashtra application sum reconciles to 1,138,055 forms; it remains explicitly labelled intake, not unique people or outcomes.
- Maharashtra signed extension replaces the reporting-only source status. Gazette publication remains unverified.
- Internal link, fragment, source-reference and JavaScript syntax checks repeated for this edition.

## Edition 1.2 full audit

- Inspected the complete jurisdiction dataset and published article inventory.
- Reconciled every Uttarakhand district equation and the four statewide column totals against rendered annexure pages 3–4. Source bytes fingerprinted in the ledger.
- Reviewed West Bengal primary orders and standard Form 6 wording; legal compilation defect recorded.
- Rebuilt data-backed sections to eliminate article/data divergence.
- No national wrongful-exclusion count, legal-compliance certification, independent ECINet audit or completed person-level investigation is claimed.
- Source retrieval failures and pending originals remain visible in the evidence and gap registers.

## Reader experience redesign

- Replaced the fixed desktop sidebar with top navigation and a keyboard-accessible menu.
- Added system-aware dark/light themes, saved reading lists on the current device, reading progress, expandable claim summaries and a dated timeline.
- Rebuilt the homepage around introductory reading paths, evidence and state discovery.
- Node DOM-harness checks passed for theme persistence, state filtering/empty results, opening and closing menu/search, saved-page toggling and reading progress. These checks do not verify browser rendering.
- Research renderer tested for idempotency and applies the shared design after rebuilding research pages.
- Research JSON is unchanged by this redesign. No new factual research is claimed.
- Reproduce interaction checks with `node scripts/ui-smoke.cjs`. Browser layout, assistive technology and touch-device inspection remain outstanding.
