# Plan: Transition to Astro + Tailwind + Airtable (Modern Stack)

## Objective
Rebuild the "Urdu Poetry Circle" archive as a true "Modern Literary Journal" using a professional frontend stack (Astro + Tailwind CSS) and an automated data backend (Airtable + `uv`). This will provide a visually stunning, high-performance site that is easy to maintain and has zero "documentation" baggage.

## Key Files & Context
- `legacy/`: All current MkDocs files.
- `src/`: Astro source code (Layouts, Components, Pages).
- `src/content/`: Local cache of poems and poet data (JSON/Markdown).
- `fetch_data.py`: A `uv`-managed Python script that syncs Airtable data to the local `src/content/`.
- `tailwind.config.mjs`: Bespoke editorial design tokens.
- `package.json`: Astro and Tailwind dependencies.
- `.github/workflows/deploy.yml`: Automated CI/CD for GitHub Pages.

## Proposed Solution

### 1. Aesthetic Direction (Option 2 Redux)
- **Framework:** Astro (Static Site Generation).
- **Styling:** Tailwind CSS (Custom typography and grid).
- **Navigation:** Custom horizontal "Journal-style" masthead.
- **Poetry Display:** Centered, oversized Nastaliq calligraphy with responsive line-spacing.

### 2. Data Strategy (`uv` + Python)
- Instead of manual file management, `uv` will run a `fetch_data.py` script.
- This script will fetch all poems and poets from Airtable via its API.
- Data is saved as structured JSON or Markdown in `src/content/`, allowing Astro to generate pages automatically.

### 3. Layout Architecture
- `Layout.astro`: Global wrapper (Typography, Masthead, Footer).
- `PoemCard.astro`: Minimalist editorial cards for index pages.
- `src/pages/index.astro`: Hero landing page with a featured couplet.
- `src/pages/poets/[poet].astro`: Dynamic poet index pages.
- `src/pages/poems/[slug].astro`: Dynamic poem reading pages.

## Implementation Steps

### Phase 1: Preparation & Scaffolding
1.  **Move Legacy Files**: Move all current MkDocs files to `legacy/`.
2.  **Initialize Astro**: Create a new Astro project in the root.
3.  **Install Tailwind**: Add Tailwind CSS to the Astro project.

### Phase 2: Data Backend (`uv`)
4.  **Create `fetch_data.py`**: A `uv`-managed script to pull data from Airtable.
5.  **Mock Data**: Create a sample `src/content/poems.json` for initial development.

### Phase 3: "Modern Journal" Frontend
6.  **Global Styles**: Setup Tailwind with `Libre Baskerville`, `Inter`, and `Jameel Noori Nastaleeq`.
7.  **Core Components**: Build the Masthead, Poem Layout, and Poet Grid.
8.  **Dynamic Pages**: Implement the index, poet, and poem routes.

### Phase 4: CI/CD & GitHub Pages
9.  **GitHub Actions**: Setup a workflow that runs `uv fetch_data.py` -> `npm build` -> `GitHub Pages Deploy`.

## Verification & Testing
1.  **URL Integrity**: Ensure that slugs (e.g., `/poets/ghalib/`) are clean and work consistently.
2.  **Visual Audit**: Verify the editorial "Paper & Ink" contrast and oversized typography on mobile.
3.  **Data Sync**: Test that adding a row in Airtable (or the mock JSON) generates a new page on build.

## Rollback Strategy
- The current MkDocs site is preserved in `legacy/`. We can revert the `mkdocs.yml` and `docs/` folder to the root at any time.
