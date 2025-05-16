import pandas as pd
import utils
import ast

tourismflanders = pd.read_excel("Final_results.xlsx", sheet_name="TourismFlanders", engine="openpyxl")
combinedAirbnb = pd.read_excel("Final_results.xlsx", sheet_name="CombinedListingsInsideAirBNB",
                               engine="openpyxl")
capacityHash = pd.read_excel("other_locations.xlsx", sheet_name="Sheet1", engine="openpyxl")

def capacity_hashmap(hashmap, TF, CA):
    TF.set_index('business_product_id', inplace=True)
    CA.set_index('id', inplace=True)

    for _, key in hashmap.iterrows():
        print(key["Key"])
        row = TF.loc[key["Key"]]
        capacity = row["maximum_capacity"]
        value_list = ast.literal_eval(key["Value"])
        updated_list = [i for i in value_list if capacity == CA.loc[i]["accommodates"]]
        hashmap.at[key.name, "Value"] = str(updated_list)  # Update the Value column with the new list
    return hashmap
capHash = capacity_hashmap(capacityHash,tourismflanders,combinedAirbnb)
utils.export_cap_hashmap_to_excel(capHash,"caphashmap.xlsx")