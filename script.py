import argparse
import csv
import logging
import sys
from pathlib import Path
from typing import Any

import requests
import unidecode
from dateutil.parser import parse

BASE_URL = "https://api.airtable.com/v0/appO8MBTJjB5BJNr9/Catalog"

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


def get_records(api_key: str) -> Any | None:
    headers = {"Authorization": api_key}
    params = {
        "maxRecords": "10",
        "view": "Grid view",
        "filterByFormula": "Status!='Added'",
    }
    logger.info("Fetching records from Airtable")
    response = requests.get(
        BASE_URL,
        params=params,
        headers=headers,
    )
    if response.ok:
        data = response.json()["records"]
        logger.info(f"Fetched: {len(data)}")
        return data


def update_record(api_key: str, record_ids: list) -> int:
    headers = {"Authorization": api_key}
    records_to_update = []
    for r_id in record_ids:
        record = {
            "id": r_id,
            "fields": {
                "Status": "Added",
            },
        }
        records_to_update.append(record)
    json_data = {"records": records_to_update}
    logger.info(f"Updating Records: {records_to_update}")
    response = requests.patch(
        BASE_URL,
        headers=headers,
        json=json_data,
    )
    return response.status_code


def read_file(file_path: str) -> list[dict]:
    rows = []
    with open(file_path, mode="r", encoding="utf-8-sig") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            rows.append(line)
    return rows


def generate_yt_embedded(link: str) -> str:
    logger.info("Generating Youtube link")
    if "youtube" in link:
        if link.startswith("<"):  # links from API start with this
            link = link.strip()
            link = link[1 : len(link) - 1]
        embedded = link.replace("watch?v=", "embed/")
        return f"""<iframe width="560" height="315" src="{embedded}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
    else:
        return link


def generate_music_section(item: dict, file) -> None:
    logger.info("Generating Music Section")
    file.write("### Renditions & Recitations\n\n")
    music_links = item["Music"].split("- ")[1:]
    for link in music_links:
        if link:
            text_link = link.split(":", 1)
            heading = text_link[0].strip()
            file.write(f"#### {heading}\n\n")
            yt_link = generate_yt_embedded(text_link[1].strip())
            file.write(f"{yt_link}\n\n")


def generate_text_section(item, file) -> None:
    logger.info("Generating Text Section")
    rekhta = f"[Rekhta]({item['Rekhta']})\n\n" if item.get("Rekhta") else None
    fran = f"[Desertful of Roses]({item['Fran']})\n\n" if item.get("Fran") else None
    if fran and rekhta:
        file.write(fran)
        file.write(rekhta)
    elif fran:
        file.write(fran)
    elif rekhta:
        file.write(rekhta)
    else:
        file.write("")


def generate_others(item: dict, file) -> None:
    logger.info("Generating Others Section")
    file.write("### Others\n\n")
    other_links = item["Others"].split("- ")[1:]
    for link in other_links:
        if link and "youtube" in link:
            text_link = link.split(":", 1)
            file.write(f"#### {text_link[0].strip()}\n\n")
            yt_link = generate_yt_embedded(text_link[1].strip())
            file.write(f"{yt_link}\n\n")
        else:
            text_link = link.split(":", 1)
            heading = text_link[0].strip()
            file.write(f"#### {heading}\n\n")
            yt_link = text_link[1].strip()
            file.write(f"{yt_link}\n\n")


def format_date(dt: str) -> str:
    parse_date = parse(dt)
    desired_format = parse_date.strftime("%Y-%m-%d")
    return desired_format


def format_ghazal(ghazal_to_format: str) -> str:
    ghazal = unidecode.unidecode(ghazal_to_format)  # remove accents
    chars_to_replace = [".", "ʾ", "`"]
    for chars in chars_to_replace:
        ghazal = ghazal.replace(chars, "")
    return ghazal


def generate_md(field: dict, poets_dir_path: Path):
    poet_path = Path.joinpath(poets_dir_path, field["Poet"])
    poet_path.mkdir(exist_ok=True)
    ghazal = field["Ghazal/Nazm"]
    ghazal = format_ghazal(ghazal_to_format=ghazal)
    ghazal_path = Path.joinpath(poet_path, ghazal)
    logger.info(f"Generating Ghazal Markdown: {ghazal}")
    date_read = format_date(field["Date"])
    with open(ghazal_path.with_suffix(".md"), "w") as file:
        boiler_text = (
                f"---\n"
                f"tags:\n"
                f"  - {date_read}\n"
                f"---\n"
                f"# {ghazal}\n\n"
                f"### Text\n"
            )
        file.writelines(boiler_text)
        generate_text_section(field, file)
        if field.get("Music"):
            generate_music_section(field, file)
        if field.get("Others"):
            generate_others(field, file)


def generate_md_from_api(records: list, poets_dir_path: Path) -> list[str]:
    record_ids = []
    for record in records:
        field = record["fields"]
        generate_md(field=field, poets_dir_path=poets_dir_path)
        record_ids.append(record["id"])
    return record_ids


def generate_md_from_file(file_path: str, poets_dir_path: Path) -> None:
    rows = read_file(file_path)
    for item in rows:
        generate_md(field=item, poets_dir_path=poets_dir_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Path, or API Key")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file-path", type=str, help="Path to csv catalog")
    group.add_argument("--api-key", type=str, help="Airtable's API Key")
    parser.add_argument(
        "--poets-dir-path",
        type=str,
        help="Path to Poet's directory where markdown files will be generated",
        required=True,
    )
    args = parser.parse_args()
    poets_dir_path = Path(args.poets_dir_path)
    if args.api_key:
        records = get_records(args.api_key)
        records_to_update = generate_md_from_api(records, poets_dir_path)
        update_record(args.api_key, records_to_update)
    if args.file_path:
        generate_md_from_file(args.file_path, poets_dir_path)
