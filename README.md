# THE SIR FILES

A chronological explanation of India’s Special Intensive Revision of electoral rolls. Events covered through 17 October 2026.

## Structure

- The story: one complete article on the homepage, from the legal background through Bihar, expansion, court decisions and October developments.
- Timeline: dated events, in order.
- States: direct links to 36 state and Union Territory reports and notes.
- Forms & law: procedure, Forms 6, 7 and 8, the legal framework and the courts.
- Documents: source links and their qualifications.
- About: scope, corrections and additional reference material.

One fixed dark palette. Serif article typography. No theme switch, case-study routes, chapter loops, saved-reading interface or hidden menu. The six menu items stay visible on mobile. Ten previous entry URLs redirect once to the story or relevant state report.

## Data and verification

`assets/research-data.json` contains 44 source records, 23 checked claims, 36 jurisdictions and the correction history. Source records include copies and unverified links; they are not counts of independent corroboration. Eight state reports have detailed analysis; 28 remain brief reference notes. No national total of wrongful exclusions is established.

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
