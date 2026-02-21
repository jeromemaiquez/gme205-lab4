from analysis import *
import json

fp_parcels = "data/parcels.json"

with open(fp_parcels, "r") as file:
    parcels_data = json.load(file)
# print(parcels_data[:2])

print(total_active_area(parcels_data))