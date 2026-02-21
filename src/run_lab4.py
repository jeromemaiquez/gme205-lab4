import analysis as a
from spatial import Parcel
import json

fp_parcels = "data/parcels.json"
fp_output = "output/summary.json"

# Load parcel data from JSON file
with open(fp_parcels, "r") as file:
    parcels_data = json.load(file)

# Convert parcels into Parcel objects
parcels = [Parcel.from_dict(parcel) for parcel in parcels_data]

if len(parcels) == 0:
    raise IndexError("List of parcels is empty")

# Define threshold area for parcels_above_threshold()
threshold_area = 300    # See README for rationale behind selected threshold

# Define target zone for intersecting_parcels()
target_zone = "Residential"

# Display analysis functions
total_active_area = a.total_active_area(parcels)
large_parcels = a.parcels_above_threshold(parcels, threshold_area)
count_per_zone = a.count_by_zone(parcels)
intersecting_parcels = a.intersecting_parcels(parcels, target_zone)

# Print results
print("Total area of active parcels: ", total_active_area)
print("List of parcels above area threshold: ", large_parcels)
print("Number of parcels per zone type: ", count_per_zone)
print("List of parcels intersecting target zone: ", intersecting_parcels)

# Save summary to output/summary.json
summary = {
    "total_active_area": total_active_area,
    "parcels_above_threshold": large_parcels,
    "count_by_zone": count_per_zone,
    "intersecting_parcels": intersecting_parcels 
}

with open(fp_output, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print(f"\nSaved summary to {fp_output}")


