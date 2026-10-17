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

## Theme repair and layout revision

- Theme selection now runs in an independent head script. Explicit themes set both palette and native colour scheme.
- Buttons show the target theme, including on narrow screens.
- Asset URLs include content hashes to prevent a newly loaded page from reusing an earlier CSS or JavaScript version.
- Theme checks pass for 16 combinations of system appearance, stored preference and blocked browser storage, including repeated toggles.
- Homepage now leads with an evidenced Goa comparison, followed by short reading paths and the state explorer. The timeline shows four recent entries with a link to the complete history.
- Research data remains unchanged. Link validation, interaction harness and renderer idempotency checks pass.
- No rendered browser or touch-device inspection was available. These are functional and structural checks, not visual verification.
- Reproduce with `node scripts/theme-check.cjs`, `node scripts/ui-smoke.cjs` and `python3 scripts/validate.py`.

## Editorial research edition 1.3

- 54 research/navigation pages plus the 404 page. 44 source records, 23 claims and 36 jurisdiction files.
- Delhi court order PDF downloaded from two publishers. Both SHA-256 fingerprints equal `a2eb7da066bbac363a8c3ddc6f055990ca40d923003f8a99febd50187cd3147f`. Text inspected; pages 3–4 visually reviewed. This is not a cryptographic-signature or Court-portal verification.
- New ECI statutory compilation inspected as indexed text. Direct PDF retrieval returned HTTP 406. Delhi candidate schedule retrieval returned HTTP 502. Both limits are disclosed.
- Internal links, fragments, data equations, CSV count and correction coverage pass. Research rendering is idempotent across generated and retained pages.
- Independent theme tests cover 16 system/storage combinations. Interaction smoke checks cover search, menu, state filters, saved reading and progress.
- Layout uses responsive editorial grids, native details elements, readable article typography and contents menus. Browser rendering and touch-device inspection remain unverified because the browser control capability is unavailable.

## Single-theme, case-led edition

Current checks: `python3 scripts/validate.py`, `python3 scripts/validate_cases.py` and `node scripts/ui-smoke.cjs`. Earlier theme-switch checks describe historical editions; the switch and its test script are now retired.

- 64 research/navigation pages plus a 404 page. Four groups, eight case overviews and 17 connected supporting chapters.
- Every case contains the question, sequence, established evidence, limits, open evidence, chapters and source record.
- Each supporting chapter has one unambiguous primary case, a chapter number, a return link and a next step.
- All HTML pages use one light palette. No theme script or switch remains. CSS does not respond to system colour preference.
- Case hub filters combine place/text and thematic group, with a result count and empty state. Existing search, menu, saved-reading and state-filter checks pass.
- Full render tested for idempotency; research JSON unchanged. Link, fragment and source-reference checks pass. Browser and touch-device visual inspection remain unavailable.

## Basic chronological edition, 18 October 2026

Current checks are `python3 scripts/validate.py`, `python3 scripts/validate_structure.py` and `node scripts/ui-smoke.cjs`. Earlier appearance and case-route checks describe superseded editions.

- One homepage article with 11 sections, ordered from definitions and legal background through the 2025–2026 events and the position covered through 17 October.
- Six visible menu items on every active page. One fixed dark palette. No case overviews or circular chapter routes in the active pages.
- 55 active pages, ten one-hop legacy redirects and one 404 page. Redirects are excluded from search and sitemap.
- Source data, arithmetic checks and correction history preserved. Internal links and fragments pass.
- Search, close/escape behaviour, state filtering, source filtering and statement filtering tested in a DOM harness.
- Full rendering tested for idempotency. Browser layout and touch-device visual inspection remain unverified.

## Hamburger menu and SIR charts

- Keyboard-accessible hamburger drawer with close button, backdrop, Escape, focus return and inert background.
- DOM-harness tests cover opening/closing the menu and switching chart views, in addition to search and content filters.
- Goa stock and movement charts, all 13 Uttarakhand district figures, and the 17/16/3 scope chart render from the same dataset used by the articles. Source links and numeric labels are explicit; charts do not imply wrongful-exclusion counts.
- Structure checks compare chart markup with data-generated components and verify menu controls on every active page.
- Public articles and chronology contain SIR developments, not website or GitHub progress. Source qualifications and corrected SIR facts remain.
- Browser rendering and touch-device visual inspection remain unverified.

## Further SIR investigation, 18 October 2026

- 47 source records and 31 claims. Three additional official source records; the October press note is explicitly limited to indexed text.
- Downloaded and visually inspected both pages of the 15 July Delhi bundle and the full 19 August order. SHA-256 fingerprints recorded in the source ledger. The August order differs from the September date on its district directory listing.
- The July forwarding and attached ECI subjects contain different qualifying dates. This is recorded as a wording inconsistency, not an established eligibility error.
- Delhi application figures are 232,514 during claims and 212,400 before draft publication. No acceptance, unique-person or published-entry total is inferred.
- SSR paragraph locators checked for readable PDFs (23(c)(ii)), notice/display safeguards (13), ERO personal checking triggers (20(b)) and appeals (19). Implementation remains unverified.
- New SIR findings appear in the chronological article, Delhi state report and existing forms/procedure pages. The design is unchanged.
- Internal links, fragments, source references, data equations, chart-source consistency and existing interaction checks pass. Source access limits are retained.
