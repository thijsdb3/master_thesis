import pandas as pd
from math import *
import ast

def preprocess_further(tourismflanders,combinedAirbnb):
    tourismflanders = tourismflanders.drop(["street", "house_number", "box_number", "postal_code", "city_name"], axis=1)
    return [tourismflanders,combinedAirbnb]


def split(hashmap):
    missing_locations = {}
    locations = {}
    for key, val in hashmap.items():
        if val == []:
            missing_locations[key] = val
        else:
            locations[key] = val

    return missing_locations, locations


def remove_locations_without_email_match(locations,tourismflanders,combinedAirbnb):
    keys = locations["Key"] #airbnb
    values = locations["Value"] # tourismflanders
    locations = {}
    for index in range(len(keys)):
        new_values = []
        row1 = combinedAirbnb[combinedAirbnb['id'] == keys[index]]
        host_firstname = str(row1['host_name']).split()[1]
        value_list = ast.literal_eval(values[index]) # tourismflandersID
        for x in range(len(value_list)):
            row2 = tourismflanders[tourismflanders["business_product_id"] == value_list[x]]
            host_email = str(row2['email']).split()[1]
            if host_firstname.upper() in host_email.upper():
                print("this is the airbnb key:", keys[index], "this is the tourismflanders key: ",value_list[x] , "this is the host_firstName:" , host_firstname, "this is the host email:" ,host_email)
                new_values.append(value_list[x])
        locations[keys[index]] = new_values

    return locations



def export_hashmap_to_excel(hashmap, filename="hashmap.xlsx"):
    hashmap = pd.DataFrame(hashmap.items(), columns=["Key", "Value"])
    hashmap.to_excel(filename, index=False)
    print(f"✅ Hashmap exported to {filename}")
def export_cap_hashmap_to_excel(hashmap, filename="Testhashmap.xlsx"):
    hashmap = pd.DataFrame(hashmap)
    hashmap.to_excel(filename, index=False)
    print(f"✅ Hashmap exported to {filename}")
