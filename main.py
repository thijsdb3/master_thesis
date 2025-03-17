import pandas as pd
import utils
from hashmap import export_hashmap_to_excel
from hashmap import create_test_hashmap

tourismflanders = pd.read_excel("Thesis_Data_Preprocessed.xlsx", sheet_name="TourismFlanders", engine="openpyxl")
combinedAirbnb = pd.read_excel("Thesis_Data_Preprocessed.xlsx", sheet_name="CombinedListingsInsideAirBNB",
                               engine="openpyxl")

#TODO check if it can't be all done in excel
[tourismflanders,combinedAirbnb] = utils.preprocess_further(tourismflanders,combinedAirbnb)
hashmap = create_test_hashmap(combinedAirbnb,tourismflanders)
export_hashmap_to_excel(hashmap)
print(hashmap)




