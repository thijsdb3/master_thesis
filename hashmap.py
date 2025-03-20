import pandas as pd
from math import *

# will create a test hashmap of size 10 , to be able to test easily and run fast
# possible to optimize the constant operations by using numpy which uses C under the hood, but you can't avoid the O(NXM) time complexity (maybe possible with K-D tree)
# iterrows() gives index ,label with index the column name and label the value of the row , but we only care about the values
def create_test_hashmap(keyDataSet, valueDataSet):
    keys = keyDataSet
    hashmap = {row["id"]: [] for _, row in keys.iterrows()}
    for _, key in keys.iterrows():
        for _, value in valueDataSet.iterrows():
            if check_in_range(key, value, 150):
                hashmap[key["id"]].append(value["business_product_id"])
    return hashmap



# checks if  the key and value are within 150 meters of each other
# both have lat/long in wsg19884
def check_in_range(key,value, max_distance):
    lat1, lon1 =  [float(key['Latitude']),float(key['Longitude'])]
    lat2, lon2 =  [float(value["Latitude"]), float(value["Longitude"])]

    diff_lat_rad = (lat2 - lat1) * pi / 180.0
    diff_lon_rad = (lon2 - lon1) * pi / 180.0

    # haversine formula
    a = (pow(sin(diff_lat_rad / 2), 2) +
         pow(sin(diff_lon_rad / 2), 2) *
         cos(lat1) * cos(lat2))
    rad_earth = 6371
    c = 2 * asin(sqrt(a))
    distance_m = rad_earth * c * 1000
    if distance_m <= max_distance:
        return True
    else:
        return False

#TODO make this also produce a count column
def export_hashmap_to_excel(hashmap, filename="hashmap.xlsx"):
    hashmap = pd.DataFrame(hashmap.items(), columns=["Key", "Value"])
    hashmap.to_excel(filename, index=False)
    print(f"✅ Hashmap exported to {filename}")