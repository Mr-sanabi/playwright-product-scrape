import csv 
from pathlib import Path

def save_csv(output_file, records):
    if not records:
        return False
    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
        
    fields = records[0].keys()

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
    return True
