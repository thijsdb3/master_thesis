import pandas as pd

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

