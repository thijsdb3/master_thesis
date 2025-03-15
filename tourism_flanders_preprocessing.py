
import pandas as pd
from utils import construct_full_address

def process_tourismflanders(file_path="public.csv"):
    tourismflanders = pd.read_csv(file_path, sep=";")

    # Construct full address as one variable
    tourismflanders['full_address'] = tourismflanders.apply(construct_full_address, axis=1)

    # Drop unnecessary columns
    tourismflanders.drop(columns=['street', 'house_number', 'box_number', 'postal_code'], inplace=True)

    # Consistent naming between this and the airbnb dataset
    tourismflanders['latitude'] = tourismflanders['lat']
    tourismflanders['longitude'] = tourismflanders['long']
    tourismflanders.drop(columns=['lat', 'long'], inplace=True)

    # drop missing values
    tourismflanders = tourismflanders.dropna(subset=['latitude', 'longitude'])
    tourismflanders = tourismflanders[['name', 'full_address','latitude', 'longitude']]

    return tourismflanders


