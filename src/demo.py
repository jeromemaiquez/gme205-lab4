from analysis import *
from spatial import Parcel
import json

fp_parcels = "data/parcels.json"

with open(fp_parcels, "r") as file:
    parcels_data = json.load(file)
    parcels = [Parcel.from_dict(parcel) for parcel in parcels_data]
# print(parcels_data[:2])

# Testing total_active_area()
print(total_active_area(parcels))

# Testing parcels_above_threshold()
threshold_area = 300    # See README for rationale behind selected threshold
print(parcels_above_threshold(parcels, threshold_area)[0])

# Testing count_by_zone()
print(count_by_zone(parcels))

# Testing intersecting_parcels()
zone = "Residential"
print(intersecting_parcels(parcels, zone)[0])