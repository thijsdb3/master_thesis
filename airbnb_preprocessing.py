import pandas as pd


def process_airbnb(file_path="listings.csv"):
    airbnb = pd.read_csv(file_path)
    airbnb = airbnb.dropna(subset=['latitude', 'longitude'])
    airbnb = airbnb.dropna(subset=['neighbourhood_group'])
    print(airbnb[["neighbourhood_group"]])
    airbnb = airbnb[['id', 'name','latitude','longitude']]
    return airbnb


process_airbnb()