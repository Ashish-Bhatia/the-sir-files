# Publication validation, 17 October 2026 IST

## Passed

- 48 research/navigation pages plus one 404 page.
- Internal page, asset and fragment checks: zero missing targets.
- One title per HTML page; no duplicate element IDs.
- 36 jurisdiction records; source references resolve in the 31-record ledger.
- All 12 claims link to existing sources. CSV and JSON row counts agree.
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
