from analysis import *
import json

fp_parcels = "data/parcels.json"

with open(fp_parcels, "r") as file:
    parcels_data = json.load(file)
# print(parcels_data[:2])

# Testing total_active_area()
print(total_active_area(parcels_data))

# Testing parcels_above_threshold()
threshold_area = 300    # See README for rationale behind selected threshold
# print(parcels_above_threshold(parcels_data, threshold_area))

# Testing count_by_zone()
print(count_by_zone(parcels_data))

# Testing intersecting_parcels()
zone = "Residential"
print(intersecting_parcels(parcels_data, zone)[0])