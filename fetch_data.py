import os
import json
import csv
import requests
from pathlib import Path
from dateutil.parser import parse

# This script is managed by uv. 
# Usage: uv run fetch_data.py

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
BASE_ID = "appO8MBTJjB5BJNr9"
TABLE_NAME = "Catalog"

def fetch_airtable_data():
    if not AIRTABLE_API_KEY:
        return None

    all_records = []
    offset = None
    
    while True:
        url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
        params = {}
        if offset:
            params["offset"] = offset
            
        headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
        
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            print(f"Error fetching Airtable data: {response.status_code}")
            break
            
        data = response.json()
        all_records.extend(data.get("records", []))
        
        offset = data.get("offset")
        if not offset:
            break
            
    return all_records if all_records else None

def read_catalog_csv():
    csv_path = Path("catalog.csv")
    if not csv_path.exists():
        return None
    
    records = []
    with open(csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append({"fields": row})
    return records

def clean_url(url):
    if not url:
        return ""
    url = url.strip()
    # Upgrade columbia edu links to https to avoid mixed content issues
    if "columbia.edu" in url and url.startswith("http://"):
        url = url.replace("http://", "https://")
    return url

def process_data(raw_records):
    grouped = {}
    
    for record in raw_records:
        fields = record["fields"]
        title = fields.get("Ghazal/Nazm", "").strip()
        poet = fields.get("Poet", "").strip()
        
        if not title or not poet:
            continue
            
        key = f"{poet}|{title}"
        
        # Format date
        date_str = fields.get("Date", "")
        formatted_date = ""
        if date_str:
            try:
                formatted_date = parse(date_str).strftime("%Y-%m-%d")
            except:
                formatted_date = date_str

        reading = {
            "date": formatted_date,
            "music": fields.get("Music", ""),
            "others": fields.get("Others", ""),
            "pdfs": fields.get("PDFs", "")
        }

        if key not in grouped:
            grouped[key] = {
                "title": title,
                "poet": poet,
                "fran": clean_url(fields.get("Fran", "")),
                "rekhta": clean_url(fields.get("Rekhta", "")),
                "readings": [reading]
            }
        else:
            # Add new reading to existing poem
            grouped[key]["readings"].append(reading)
            # Update resources if they were missing in previous rows
            if not grouped[key]["fran"]: grouped[key]["fran"] = clean_url(fields.get("Fran", ""))
            if not grouped[key]["rekhta"]: grouped[key]["rekhta"] = clean_url(fields.get("Rekhta", ""))

    # Convert back to list and sort readings by date
    result = []
    import re
    for item in grouped.values():
        item["readings"].sort(key=lambda x: x["date"] or "0000", reverse=True)
        # Create a unique slug using robust regex
        raw_slug = f"{item['poet']}-{item['title']}".lower()
        # Replace non-alphanumeric (allowing Urdu range) with hyphens
        item["slug"] = re.sub(r'[^a-z0-9\u0600-\u06FF]+', '-', raw_slug).strip('-')
        result.append(item)
        
    return result

def update_airtable_status(record_ids):
    if not AIRTABLE_API_KEY or not record_ids:
        return
    
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    
    # Airtable allows updating up to 10 records at a time
    for i in range(0, len(record_ids), 10):
        chunk = record_ids[i:i+10]
        records = [{"id": rid, "fields": {"Status": "Added"}} for rid in chunk]
        try:
            response = requests.patch(url, headers=headers, json={"records": records})
            if response.ok:
                print(f"Successfully marked {len(chunk)} records as 'Added' in Airtable")
            else:
                print(f"Error updating status: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Failed to update Airtable: {e}")

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-refresh", action="store_true", help="Process all records regardless of status")
    args = parser.parse_args()

    raw_data = fetch_airtable_data()
    source = "Airtable"
    
    if raw_data is None:
        raw_data = read_catalog_csv()
        source = "catalog.csv"
        
    if raw_data is None:
        print("No data found.")
        return

    # If fetching from Airtable, handle status updates
    if source == "Airtable":
        to_update = [r["id"] for r in raw_data if r["fields"].get("Status") != "Added"]
        if to_update:
            print(f"Found {len(to_update)} new records to process...")
            update_airtable_status(to_update)
            # Update local state so they are included in the processing
            for r in raw_data:
                if r["id"] in to_update:
                    r["fields"]["Status"] = "Added"

    # Determine which records to process
    if args.full_refresh:
        print("Performing full refresh: processing all records.")
        records_to_process = raw_data
    else:
        records_to_process = [r for r in raw_data if r["fields"].get("Status") == "Added"]
    
    processed_data = process_data(records_to_process)
    
    # Process and save to src/content/archive
    output_dir = Path("src/content/archive")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_dir / "poems.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully processed {len(processed_data)} poems to archive.")

if __name__ == "__main__":
    main()
