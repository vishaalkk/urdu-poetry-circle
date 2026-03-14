# Plan: Urdu Poetry Circle Redesign

## Objective
Transform the current archive into a visually stunning, high-performance "Modern Literary Journal." This involves upgrading typography, enhancing layout, and improving content discovery to create a serene and elegant reading experience for Urdu poetry.

## Key Files & Context
- `mkdocs.yml`: Theme and plugins configuration.
- `docs/stylesheets/extra.css`: Global styles, typography, and layout.
- `docs/index.md`: Homepage redesign.
- `docs/poets.md`: Poet index page.
- `docs/poets/`: Standardized poem page structure.

## Proposed Solution

### 1. Aesthetic Direction: "Modern Literary Journal"
- **Tone:** Refined Minimalism / Literary Archive.
- **Color Palette:**
    - **Background:** Cream/Off-white (`#fcfaf2`) for a "paper" feel.
    - **Text:** Deep Ink/Charcoal (`#1c1c1c`).
    - **Accents:** Deep Teal (`#004d40`) or Antique Maroon (`#6d1a1a`).
- **Typography:**
    - **Urdu:** `Jameel Noori Nastaleeq` (web-font) or `Noto Nastaliq Urdu` fallback.
    - **Serif (English/Transliteration):** `Playfair Display` for titles and `Lora` for body text.
    - **Sans-Serif (UI/Nav):** `Inter`.

### 2. Homepage (`docs/index.md`)
- **Hero Section:** A minimalist hero with a poetic quote in Urdu (Nastaleeq) and English.
- **Featured Poets:** Visual cards for major poets like Faiz and Ghalib using existing images.
- **Recent Additions:** A subtle list or grid of the latest poems added to the archive.

### 3. Poet Index (`docs/poets.md`)
- **Editorial Grid:** Redesign the poet cards to include initials or placeholder silhouettes for poets without photos.
- **Refined Cards:** Use better shadows, borders, and typography for a "gallery" look.

### 4. Poem Pages (`docs/poets/.../*.md`)
- **Standardized Layout:**
    - **Title:** Large Serif title.
    - **Poetry Body:** Centered, wide-spaced Urdu text in Nastaleeq.
    - **Transliteration:** Elegant Serif text below each Urdu couplet (or as a separate section).
    - **Performance Section:** Clean, centered YouTube embeds with a "card" style container.
- **Metadata:** Subtle display of tags (date, mood, etc.) and poet name.

### 5. Global Styles (`docs/stylesheets/extra.css`)
- Implement the "Paper & Ink" theme.
- Add responsive font scaling for better readability on all devices.
- Refine the navigation bar with a cleaner, more minimalist design.

## Implementation Steps

### Phase 1: Foundation (Styling & Config)
1.  **Update `mkdocs.yml`**: Configure the `material` theme for the new color palette and enable advanced features (tabs, search).
2.  **Enhance `extra.css`**: Define global variables for colors, typography, and spacing. Implement the Nastaleeq font stack.

### Phase 2: Visual Overhaul (Homepage & Index)
3.  **Redesign `index.md`**: Create the new hero section and featured poet cards.
4.  **Redesign `poets.md`**: Update the poet grid with the new card styles.

### Phase 3: Content Refinement (Poem Pages)
5.  **Create a Poem Template**: Establish a standard Markdown structure for poem files to ensure consistent rendering.
6.  **Update Sample Poems**: Apply the new template to a few key poems (e.g., Ghalib, Faiz) to demonstrate the design.

## Verification & Testing
1.  **Visual Audit**: Check the site on desktop and mobile to ensure typography and layout are correct.
2.  **Performance Check**: Ensure fonts load correctly and don't slow down the site significantly.
3.  **Cross-Browser Testing**: Verify Nastaleeq rendering on different browsers (Chrome, Safari, Firefox).

## Rollback Strategy
- Keep a backup of the original `mkdocs.yml` and `extra.css`.
- Revert changes to Markdown files if the new template is not desired.
