# Plan: Modern Literary Journal (Option 2) Redesign

## Objective
Transform the site into a high-end, minimalist "Modern Literary Journal" (e.g., *The New Yorker*, *Granta*). This involves a radical departure from the "documentation" look: killing sidebars, using high-contrast editorial colors, and employing oversized typography.

## Key Files & Context
- `mkdocs.yml`: Theme and layout configuration (Global hide).
- `docs/stylesheets/extra.css`: Master typography and editorial layout.
- `overrides/main.html`: Custom Jinja2 template to override the default MkDocs navigation and structure.
- `docs/index.md`: Minimalist hero couplet homepage.
- `docs/poets/`: Magazine-style poet and poem pages.

## Proposed Solution

### 1. Aesthetic Direction: "Modern Literary Journal"
- **Color Palette (Editorial):**
    - **Background:** High-Contrast Cream (`#F9F7F2`) for a premium "book" feel.
    - **Text:** Deep Obsidian/Charcoal (`#080808`).
    - **Accent:** A single, sharp accent (e.g., Deep Crimson `#9B1B30` or Midnight Blue `#003366`) used very sparingly.
- **Typography (Oversized & Bold):**
    - **Urdu:** `Jameel Noori Nastaleeq` (2.5rem - 4rem for titles/quotes).
    - **Primary Serif:** `Libre Baskerville` or `Baskerville` (Classic, literary feel).
    - **UI Sans:** `Inter` (Very light weights, e.g., 300).

### 2. Layout Overhaul (Sidebar-Free)
- **Kill Global Sidebar:** Use MkDocs `hide` tags and CSS to remove navigation and TOC sidebars globally.
- **Top Navigation:** Create a custom, minimalist "Masthead" centered at the top.
- **Narrow Reading Column:** Restrict the content width to ~800px-900px, centered on the page.

### 3. Homepage (`index.md`)
- **Hero Couplet:** A massive, single Urdu couplet in center-stage. No secondary text initially.
- **Minimalist Menu:** Floating or centered links: `Poets / Archive / About`.

### 4. Poet Index & Pages
- **Visual Grid:** Clean portraits with minimalist captions.
- **Poet Bio:** Large serif text, centered.

### 5. Poem Pages
- **Title:** Oversized, italicized serif.
- **Poetry:** Wide line-spacing, centered Nastaliq.
- **Metadata:** Subtle, small caps at the very bottom.

## Implementation Steps

### Phase 1: Structural Changes
1.  **Configure `overrides/`**: Create a custom `main.html` to strip down the default header and sidebar.
2.  **Update `mkdocs.yml`**: Configure the theme to use the `overrides/` directory and hide standard UI elements.

### Phase 2: Master Stylesheet (`extra.css`)
3.  **Implement Editorial CSS**:
    - High-contrast color variables.
    - Global sidebar removal (`.md-sidebar--primary { display: none; }`).
    - Responsive, oversized typography using `clamp()`.
    - Custom centered grid system.

### Phase 3: Content Refinement
4.  **Rewrite Homepage**: A true "journal-style" landing page.
5.  **Standardize Poet/Poem Pages**: Update templates for a consistent, minimal reading experience.

## Verification & Testing
1.  **Readability Audit**: Ensure the oversized text doesn't break on mobile screens.
2.  **Navigation Flow**: Verify that the custom top-nav is intuitive without the sidebar.
3.  **Visual Consistency**: Check the "Paper & Ink" contrast across different devices.

## Rollback Strategy
- Revert `mkdocs.yml` and `extra.css` to previous versions.
- Delete the `overrides/` directory to return to the default Material theme.
