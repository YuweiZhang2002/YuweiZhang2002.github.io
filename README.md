# Evelyn Zhang / 张煜玮 — Academic Homepage

A buildless, responsive bilingual academic homepage. English: `/`; Chinese: `/zh/`.

## Content and editing

- `build.py`: bilingual copy and 16 bibliographic records. Run `python3 build.py` after changing this file.
- The Experience section replaces the former open-source project cards. Its five internships and research assistant roles, dates, supervisors, and research areas were supplied by the owner; entries are ordered by start date, newest first.
- `dist/assets/style.css`: layout and colors.
- `dist/assets/app.js`: publication filtering and search.
- `dist/assets/portrait.jpg`: portrait from the supplied public Scholar profile (the original is low resolution).
- `dist/`: complete ready-to-host static website; no package installation or build service needed.

Content was verified on 2026-10-20 against:

- https://scholar.google.com/citations?user=renmzGoAAAAJ&hl=en
- https://github.com/YuweiZhang2002
- https://github.com/YuweiZhang2002/SiTo
- https://github.com/YuweiZhang2002/DaTo
- https://github.com/YuweiZhang2002/D2Pruner

Name and public email were confirmed directly by the owner. The biography is a concise synthesis of those research topics. Education and advisor information follow the CV screenshot supplied by the owner. The owner requested the date range without an “expected” qualifier. No current enrollment status, job title, awards, or unpublished projects are inferred. Email is already published in the SiTo README. Years follow Scholar, including its 2024 entry for DaTo (arXiv:2501.00375). The list preserves separate Scholar records that may be preprint and publication versions of related work. Long author lists use “et al.” as in the visible record.

## Preview

Run `python3 -m http.server 8917 --directory dist` and open http://localhost:8917/ .

## GitHub Pages

Intended account: `YuweiZhang2002`.
Intended personal-homepage repository: `YuweiZhang2002.github.io`.
The intended URL, once deployed successfully, is https://yuweizhang2002.github.io/ . This is not a claim that publication has completed.

Option A (no Actions): upload the **contents** of `dist/` to the root of the `main` branch of that repository. In Settings → Pages, choose “Deploy from a branch”, `main`, `/ (root)`, then Save.

Option B (source + Actions): put this project in the repository, including `.github/workflows/pages.yml`. In Settings → Pages select “GitHub Actions”. Push to `main` or run the “Deploy academic homepage” workflow. The workflow publishes `dist/`.

The `.openai` directory is only for the separate Sites preview and is not required by GitHub Pages.

## Publication figures and school marks

The owner confirmed NeurIPS 2026 for Focused Forcing and HiLoc. HiLoc metadata follows the camera-ready manuscript and its public project website. GRIT, Occlusion Is Underrated, and Robust Traffic Light Recognition were removed at the owner’s explicit request.

`paper-media.json` records each reproduced paper figure, original source, and preview asset. All 16 entries use actual paper figures or author-published previews. The linear-attention survey uses its chunkwise parallel computation figure; the accessible author PDF does not contain an overview taxonomy. AMID uses its coauthor’s framework preview. Preprint/publication title and version differences are recorded in the manifest. Figures are reproduced without altering their scientific content; rights remain with the original authors/publishers.

`school-logos.json` records the three official university marks and their sources. Preserve their aspect ratios.

`institution-logos.json` records the five internship institution logos and their sources. The IEG white wordmark uses a dark backing for contrast; all logos preserve their original proportions and colors.

The GitHub Pages site is live at https://yuweizhang2002.github.io/ (English) and https://yuweizhang2002.github.io/zh/ (Chinese).
