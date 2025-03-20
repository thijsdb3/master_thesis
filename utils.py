import pandas as pd
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


#this is a lot of battling with types xD
def remove_locations_without_email_match(locations,tourismflanders,combinedAirbnb):
    keys = locations["Key"]
    values = locations["Value"]
    locations = {}
    for index in range(len(keys)):
        new_values = []
        row1 = combinedAirbnb[combinedAirbnb['id'] == keys[index]]
        host_firstname = str(row1['host_name']).split()[1]
        value_list = ast.literal_eval(values[index])
        for x in range(len(value_list)):
            row2 = tourismflanders[tourismflanders["business_product_id"] == value_list[x]]
            host_email = row2['email']
            if host_firstname in str(host_email):
                new_values.append(value_list[x])

        locations[keys[index]] = new_values

    return locations

