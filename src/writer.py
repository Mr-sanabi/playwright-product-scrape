import csv 

def save_csv(output_file, records):
    if not records:
        return
        
    fields = records[0].keys()

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)    