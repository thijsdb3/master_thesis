import pandas as pd
from utils import *
from hashmap import *
tourismflanders = pd.read_excel("Thesis_Data_Preprocessed.xlsx", sheet_name="TourismFlanders", engine="openpyxl")
combinedAirbnb = pd.read_excel("Thesis_Data_Preprocessed.xlsx", sheet_name="CombinedListingsInsideAirBNB",
                               engine="openpyxl")
locations = pd.read_excel("other_locations.xlsx", engine="openpyxl")
locations = remove_locations_without_email_match(locations,tourismflanders,combinedAirbnb)
[missed_locations,other_locations] = split(locations)

export_hashmap_to_excel(other_locations, "other_locations_after_email_matching.xlsx")
export_hashmap_to_excel(missed_locations,"missing_locations_after_email_matching.xlsx")

