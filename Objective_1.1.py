import pandas as pd
from utils import *
from hashmap import export_hashmap_to_excel
from hashmap import create_test_hashmap
tourismflanders = pd.read_excel("Thesis_Data_Preprocessed.xlsx", sheet_name="TourismFlanders", engine="openpyxl")
combinedAirbnb = pd.read_excel("Thesis_Data_Preprocessed.xlsx", sheet_name="CombinedListingsInsideAirBNB",
                               engine="openpyxl")

#first Objective step 1
[tourismflanders,combinedAirbnb] = preprocess_further(tourismflanders,combinedAirbnb)
hashmap = create_test_hashmap(combinedAirbnb,tourismflanders)
export_hashmap_to_excel(hashmap)

[missed_locations,other_locations] = split(hashmap)
export_hashmap_to_excel(missed_locations, "missing_locations.xlsx")
export_hashmap_to_excel(other_locations,"other_locations.xlsx")

