import csv
import os
from pathlib import Path
from urllib.parse import parse_qsl, urljoin
import unidecode

directory_path = Path('/Users/vishalk/personal-repo/urdu-poetry-circle/docs/poets')


file_path = '/Users/vishalk/Downloads/Catalog-Grid view.csv'



def read_file(file_path: str):
    # poet_count = {}
    rows = []
    with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            rows.append(line)
            # poet = line['Poet']
            # if poet in poet_count:
            #     poet_count[poet] += 1
            # else:
            #     poet_count[poet] = 1
    # poet_count = dict(sorted(poet_count.items(), key=lambda item: item[1], reverse=True))
    return rows


def generate_yt_embedded(link:str) -> str:
    if "youtube" in link:
        embedded = link.replace("watch?v=", "embed/")
        return f'''<iframe width="560" height="315" src="{embedded}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    else:
        return link


def generate_music_section(item:dict, file):
    file.write('### Renditions & Recitations\n\n')
    music_links = item['Music'].split('- ')[1:]
    for link in music_links:
        if link:
            s = link.split(':', 1)
            file.write(f'#### {s[0].strip()}\n\n')
            l = generate_yt_embedded(s[1].strip())
            file.write(f'{l}\n\n')


def generate_text_section(item, file):
    fran = f"[Desertful of Roses]({item['Fran']})\n\n"
    rekhta = f"[Rekhta]({item['Rekhta']})\n\n"
    if item['Fran'] and item['Rekhta']:
        file.write(fran)
        file.write(rekhta)
    elif item['Fran']:
        file.write(fran)
    elif item['Rekhta']:
        file.write(rekhta)
    else:
        file.write('')
        
        
def generate_others(item:dict, file):
    file.write('### Others\n\n')
    other_links = item['Others'].split('- ')[1:]
    for link in other_links:
        if link and 'youtube' in link:
            s = link.split(':', 1)
            file.write(f'#### {s[0].strip()}\n\n')
            l = generate_yt_embedded(s[1].strip())
            file.write(f'{l}\n\n')
        else:
            s = link.split(':', 1)
            file.write(f'#### {s[0].strip()}\n\n')
            l = s[1].strip()
            file.write(f'{l}\n\n')
    
    

def generate_md(file_path: str):
    rows = read_file(file_path)
    for item in rows:
        poet_path = Path.joinpath(directory_path, item['Poet'].lower())
        poet_path.mkdir(exist_ok=True)
        ghazal = item['Ghazal/Nazm']
        ghazal = ghazal.replace('.', '')  # ghazals with . in them
        ghazal = unidecode.unidecode(ghazal)  # remove accents
        ghazal_path = Path.joinpath(poet_path, ghazal)
        ghazal_file = ghazal_path.with_suffix('.md')
        with open(ghazal_path.with_suffix('.md'), 'w') as file:
            boiler_text = (
                f"***\n"
                f"Date Read: {item['Date']}\n"
                f"***\n\n"
                f"# {ghazal}\n\n"
                f"### Text\n"
            )
            file.writelines(boiler_text)
            generate_text_section(item, file)
            if item['Music']:
                # pdb.set_trace()
                # print(item['Music'])
                generate_music_section(item, file)
            if item['Others']:
                generate_others(item, file)


generate_md(file_path)
