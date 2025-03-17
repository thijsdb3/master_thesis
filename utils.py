import pandas as pd

def preprocess_further(tourismflanders,combinedAirbnb):
    # fields are only used in excel to calculate Latitude and Longitude
    # TODO if possible remove them from excel such that this line can be deleted and have consistent naming
    tourismflanders = tourismflanders.drop(["lat", "long"], axis=1)
    # fields are only used in excel to calculate latitude and longitude
    # TODO if possible remove them from excel such that this line can be deleted and have consistent naming
    combinedAirbnb = combinedAirbnb.drop(["latitude", "longitude"], axis=1)
    combinedAirbnb.rename(columns={'lat': 'latitude', 'long': 'longitude'}, inplace=True)
    # fields are redundant because of the existence of "Full address"
    tourismflanders = tourismflanders.drop(["street", "house_number", "box_number", "postal_code", "city_name"], axis=1)
    return [tourismflanders,combinedAirbnb]


