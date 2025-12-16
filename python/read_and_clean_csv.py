import csv

input_file = "data/trips_raw.csv"
output_file = "data/trips_clean.csv"

clean_rows = []

with open(input_file, mode="r") as file:
reader = csv.DictReader(file)

for row in reader:
if row["distance_miles"] and row["cost_usd"]:
row["distance_miles"] = float(row["distance_miles"])
row["cost_usd"] = float(row["cost_usd"])
clean_rows.append(row)

with open(output_file, mode="w", newline="") as file:
fieldnames = clean_rows[0].keys()
writer = csv.DictWriter(file, fieldnames=fieldnames)

writer.writeheader()
writer.writerows(clean_rows)

print("Data cleaning complete. Clean file created.")
