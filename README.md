# Columbia Urdu Poetry Group Archive

A modern, editorial-style digital archive of the Columbia Urdu Poetry Group readings.

## Tech Stack

- **Frontend:** [Astro](https://astro.build/) + [Tailwind CSS](https://tailwindcss.com/)
- **Backend:** Python + [uv](https://github.com/astral-sh/uv)
- **Data Source:** Airtable (with `catalog.csv` fallback)
- **Deployment:** GitHub Pages

## Development

### Prerequisites

- Node.js (v20+)
- Python (v3.9+)
- `uv` (for Python dependency management)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vchrombie/urdu-poetry-circle.git
    cd urdu-poetry-circle
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    uv sync
    ```

3.  **Sync data:**
    ```bash
    uv run fetch_data.py
    ```
    *Note: Set `AIRTABLE_API_KEY` in your environment to fetch from live Airtable.*

4.  **Start development server:**
    ```bash
    npm run dev
    ```

### Deployment

The site is automatically built and deployed to GitHub Pages via GitHub Actions on every push to the `main` branch.

## Legacy

Old MkDocs-based site files are preserved in the `legacy/` directory for historical reference.
