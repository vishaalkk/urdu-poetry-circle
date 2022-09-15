import csv
import os
from pathlib import Path

directory_path = Path('/Users/vishalk/Documents/projects/urdu-poetry-circle/docs/poets')
d = []

file_path = '/Users/vishalk/Downloads/Catalog-Grid view.csv'

poet_count = {}
with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        d.append(line)
        poet = line['Poet']
        if poet in poet_count:
            poet_count[poet] += 1
        else:
            poet_count[poet] = 1
    # print(csv_reader.restkey)
poet_count = dict(sorted(poet_count.items(), key=lambda item: item[1], reverse=True))

m = d[:2]

text_1 = f'''
---\n
Date Read: {item['Date']}\n
---\n\n
# {ghazal}\n\n
### Text\n
'''


def generate_yt_embedded(link:str) -> str:
    embedded = link.replace("watch?v=", "embed/")
    return f'''<iframe width="560" height="315" src="{embedded}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''


def generate_music_section(item:dict):
    file.write('### Renditions & Recitations\n\n')
    music_links = item['Music'].split('-')[1:]
    for link in music_links:
        s = link.split(':', 1)
        file.write(f'#### {s[0].strip()}\n\n')
        l = generate_yt_embedded(s[1].strip())
        file.write(f'{l}\n\n')


def generate_text_section(item):
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
        
        
def generate_others(item):
    file.write('### Others\n\n')
    

for item in n:
    poet_path = Path.joinpath(directory_path, item['Poet'].lower())
    if not poet_path.exists():
        poet_path.mkdir()
    ghazal = item['\ufeffGhazal/Nazm']
    ghazal_path = Path.joinpath(poet_path, ghazal)
    ghaza_file = ghazal_path.with_suffix('.md')
    if ghaza_file.exists():
        with open(ghazal_path.with_suffix('.md'), 'w') as file:
            text_1 = f'''
---\n
Date Read: {item['Date']}\n
---\n\n
# {ghazal}\n\n
### Text\n
'''
            # file.write('---\n')
            # file.write(f"Date Read: {item['Date']}\n")
            # file.write('---\n\n')
            # file.write(f"# {ghazal}\n\n")
            # file.write(f"### Text\n")
            file.writelines(text_1)
            generate_text_section(item)
            # if item['Fran']:
            #     file.write(f"[Desertful of Roses]({item['Fran']})\n\n")
            if item['Music']:
                generate_music_section(item)
                # file.write('### Renditions & Recitations\n\n')
                # music_links = item['Music'].split('-')[1:]
                # for link in music_links:
                #     s = link.split(':', 1)
                #     file.write(f'#### {s[0].strip()}\n\n')
                #     l = generate_yt_embedded(s[1].strip())
                #     file.write(f'{l}\n\n')
                
            
        
    




---
Date: 07-05-2021
---

# sharmā ga.e lajā ga.e dāman chhuḌā ga.e 
###### [07-15-2021](../../announcements/07-15-2021.eml)


### Text
[Rekhta](https://rekhta.org/ghazals/sharmaa-gae-lajaa-gae-daaman-chhudaa-gae-jigar-moradabadi-ghazals)




### Renditions & Recitations

#### Begum Akhtar
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6vE29v2RShQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Rochana
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/WFWTB4i9nGw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Duniya Ke Sitam - Jigar Reciting in Tarannum
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7hlYTchABes" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


