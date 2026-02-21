from spatial import Parcel

def total_active_area(parcels: list) -> float:
    total_active_area = 0
    
    for parcel_data in parcels:
        parcel = Parcel.from_dict(parcel_data)
        if parcel.is_active:
            total_active_area += parcel.area_sqm
    
    return total_active_area


def parcels_above_threshold(parcels: list, threshold: float) -> list:
    large_parcels = []

    for parcel_data in parcels:
        parcel = Parcel.from_dict(parcel_data)
        if parcel.area_sqm > threshold:
            large_parcels.append(parcel.as_dict())
    
    return large_parcels

def count_by_zone(parcels: list) -> dict:
    count_per_zone = {}
    
    for parcel_data in parcels:
        parcel = Parcel.from_dict(parcel_data)
        if parcel.zone in list(count_per_zone.keys()):
            count_per_zone[parcel.zone] += 1
        else:
            count_per_zone[parcel.zone] = 1
    
    return count_per_zone

def intersecting_parcels(parcels: list, zone: str) -> list:
    intersecting_parcels = []

    for parcel_data in parcels:
        parcel = Parcel.from_dict(parcel_data)
        if parcel.zone == zone:
            intersecting_parcels.append(parcel.as_dict())

    return intersecting_parcels