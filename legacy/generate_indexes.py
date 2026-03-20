import os
import urllib.parse
from pathlib import Path

def generate_indexes():
    docs_dir = Path("docs")
    poets_dir = docs_dir / "poets"
    
    if not poets_dir.exists():
        print(f"Directory {poets_dir} does not exist.")
        return

    poet_dirs = sorted([d for d in poets_dir.iterdir() if d.is_dir()])
    
    # 1. Update docs/poets.md
    with open(docs_dir / "poets.md", "w") as f:
        f.write("# The Poets\n\n")
        f.write('<div style="text-align: center; margin: 4rem 0;">\n')
        f.write('  <p style="font-size: 1.2rem; color: var(--journal-faded); font-style: italic;">\n')
        f.write('    An archive of the masters of Urdu verse, spanning centuries and styles.\n')
        f.write('  </p>\n')
        f.write('</div>\n\n')
        
        # Featured poets section
        f.write('<div class="poet-grid">\n')
        featured = ["Ghalib", "Faiz Ahmed Faiz", "Jaun Elia", "Parveen Shakir", "Ahmad Faraz", "Sahir Ludhianvi"]
        for p in featured:
            p_dir = poets_dir / p
            if p_dir.exists():
                img_path = f"../images/{p.lower().replace(' ', '_')}.jpg"
                img_exists = (docs_dir / "images" / f"{p.lower().replace(' ', '_')}.jpg").exists()
                if p == "Ghalib": img_exists, img_path = True, "../images/ghalib.jpg"
                if p == "Faiz Ahmed Faiz": img_exists, img_path = True, "../images/faiz.jpg"
                
                encoded_p = urllib.parse.quote(p)
                f.write(f'  <a href="{encoded_p}/" class="poet-card">\n')
                if img_exists:
                    f.write(f'    <img src="{img_path}" alt="{p}" class="poet-image">\n')
                else:
                    initial = p[0]
                    f.write(f'    <div class="poet-image" style="background: #EAE8E3; display: flex; align-items: center; justify-content: center; font-size: 3rem; font-family: var(--font-serif);">{initial}</div>\n')
                f.write(f'    <div class="poet-name">{p}</div>\n')
                f.write('  </a>\n')
        f.write('</div>\n\n')
        
        # Complete Catalog
        f.write('<div style="margin-top: 8rem; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 4rem;">\n')
        f.write('  <h2>Complete Catalog</h2>\n')
        f.write('  <div style="column-count: 3; column-gap: 2rem; margin-top: 2rem;">\n')
        for p_dir in poet_dirs:
            p_name = p_dir.name
            encoded_p = urllib.parse.quote(p_name)
            # Use Markdown link for better resolution
            f.write(f'    [{p_name}]({encoded_p}/){{ .catalog-link }}\n\n')
        f.write('  </div>\n')
        f.write('</div>\n')

    # 2. Update each poet's index.md
    for p_dir in poet_dirs:
        p_name = p_dir.name
        poems = sorted([f for f in p_dir.iterdir() if f.suffix == ".md" and f.name != "index.md"])
        
        bio = ""
        index_file = p_dir / "index.md"
        if index_file.exists():
            content = index_file.read_text()
            if "---" in content:
                bio = content.split("---")[0].strip()
            else:
                bio = f"# {p_name}\n"
        
        if not bio:
            bio = f"# {p_name}\n"

        with open(index_file, "w") as f:
            f.write(bio)
            f.write("\n\n---\n\n")
            f.write("## Selected Readings\n\n")
            f.write('<div style="text-align: center; font-family: var(--font-serif); font-size: 1.1rem; margin-top: 2rem;">\n\n')
            for poem in poems:
                poem_title = poem.stem
                encoded_name = urllib.parse.quote(poem.name)
                # Pure Markdown link with attribute
                f.write(f'[{poem_title}]({encoded_name}){{ .poem-link }}\n\n')
            f.write('</div>\n')

if __name__ == "__main__":
    generate_indexes()
