import pandas as pd

def preprocess_further(tourismflanders,combinedAirbnb):
    tourismflanders = tourismflanders.drop(["street", "house_number", "box_number", "postal_code", "city_name"], axis=1)
    return [tourismflanders,combinedAirbnb]


