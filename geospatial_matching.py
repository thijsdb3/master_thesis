from math import pi, sin, cos, sqrt, asin
import pandas as pd
import geospatial_matching as gm

def create_dictionary(Tourism_Flanders, inside_airbnb):
    hashmap = {row["business_product_id"]: [] for _, row in Tourism_Flanders.iterrows()}

    for _, tf_row in Tourism_Flanders.iterrows():
        for _, airbnb_row in inside_airbnb.iterrows():
            if check_in_range(tf_row, airbnb_row, 100):
                hashmap[tf_row["business_product_id"]].append(airbnb_row["id"])

    return hashmap

def check_in_range(key, value, max_distance):
    lat1, lon1 = float(key['lat']), float(key['long'])
    lat2, lon2 = float(value["latitude"]), float(value["longitude"])

    # Convert latitude and longitude from degrees to radians
    lat1_rad, lon1_rad = lat1 * pi / 180.0, lon1 * pi / 180.0
    lat2_rad, lon2_rad = lat2 * pi / 180.0, lon2 * pi / 180.0

    diff_lat_rad = lat2_rad - lat1_rad
    diff_lon_rad = lon2_rad - lon1_rad

    # haversine Formula
    a = (sin(diff_lat_rad / 2) ** 2 +
         sin(diff_lon_rad / 2) ** 2 * cos(lat1_rad) * cos(lat2_rad))
    radius_earth = 6371  # in kilometers
    c = 2 * asin(sqrt(a))
    distance_m = radius_earth * c * 1000

    return distance_m <= max_distance





tourismflanders = pd.read_excel("TestingIndex.xlsx", sheet_name="TourismFlanders", engine="openpyxl")
combinedAirbnb = pd.read_excel("TestingIndex.xlsx", sheet_name="CombinedListingsInsideAirBNB",
                               engine="openpyxl")

[tourismflanders,combinedAirbnb] = gm.preprocess_further(tourismflanders,combinedAirbnb)
hashmapTF = gm.create_dictionary(tourismflanders,combinedAirbnb)
gm.export_hashmap_to_excel(hashmapTF)

[missed_locations,other_locations] = gm.split(hashmapTF)
gm.export_hashmap_to_excel(missed_locations, "missing_locations.xlsx")
gm.export_hashmap_to_excel(other_locations,"other_locations.xlsx")