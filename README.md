# THE SIR FILES

A chronological explanation of India’s Special Intensive Revision of electoral rolls. Events covered through 17 October 2026.

## Structure

- The story: one complete article on the homepage, from the legal background through Bihar, expansion, court decisions and October developments.
- Timeline: dated events, in order.
- States: direct links to 36 state and Union Territory reports and notes.
- Forms & law: procedure, Forms 6, 7 and 8, the legal framework and the courts.
- Documents: source links and their qualifications.
- SIR basics: how to read omissions, applications, decisions and roll changes.

One fixed dark palette. Serif article typography. No theme switch, case-study routes, chapter loops or saved-reading interface. A hamburger drawer contains the same six menu items on desktop and mobile. Ten previous entry URLs redirect once to the story or relevant state report.

## Data and verification

`assets/research-data.json` contains 47 source records, 31 checked claims, 36 jurisdictions and the correction history. Source records include copies and unverified links; they are not counts of independent corroboration. Eight state reports have detailed analysis; 28 remain brief reference notes. No national total of wrongful exclusions is established.

After changing the data or article templates:

```sh
python3 scripts/render_research.py
python3 scripts/validate.py
python3 scripts/validate_structure.py
node scripts/ui-smoke.cjs
```

The renderer builds the state reports, source list, chronological article, timeline and guides. It excludes old redirect pages from search and sitemap. Rendering is idempotent. Browser layout and touch-device inspection remain unverified in this environment.

## Publishing

GitHub Pages: deploy from branch `main`, root directory. The site is buildless and uses `.nojekyll`. No custom Actions workflow, API key, package installation or server is required. GitHub runs its normal Pages build and deployment process.

https://ashish-bhatia.github.io/the-sir-files/

## SIR charts and navigation

The hamburger menu supports close, backdrop click, Escape, focus return and keyboard focus containment. Background content is inert while the menu is open.

Sourced interactive charts show Goa roll sizes and draft-to-final movements, Uttarakhand final rolls and changes across all 13 districts, and the 17/16/3 revision-stage groups in the 15 October ECI order. Values come directly from the research dataset. All count bars begin at zero; signed changes use a central zero line. Figures and source links remain visible.

The public pages contain SIR information and source qualifications. Website development, publishing and GitHub updates are excluded. Internal correction history remains in the data and Git history; factual corrections are incorporated into the SIR explanations.

## Delhi and SSR source follow-up, 18 October 2026

Two signed Delhi schedule bundles were downloaded and visually inspected. The July and August targets remain explicitly historical. The district listing date is not substituted for the August order date. The July covering and attached-order subjects contain different qualifying dates, with no inferred individual outcome.

The 17 October CEO note is available as indexed official text. Full PDF retrieval returned HTTP 502. Its 232,514 and 212,400 Form 6 figures are shown only as applications in different periods, with no deduplication or registration-outcome claim.

The 15 October SSR order is now explained for readable PDF distribution, notice and waiting-period safeguards, ERO cross-check triggers and appeals. Directions remain separate from implementation evidence. No design or navigation change accompanies this research update.
