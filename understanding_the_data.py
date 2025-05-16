
import pandas as pd

tourismflanders = pd.read_excel("Final_results.xlsx", sheet_name="TourismFlanders", engine="openpyxl")
combinedAirbnb = pd.read_excel("Final_results.xlsx", sheet_name="CombinedListingsInsideAirBNB",
                               engine="openpyxl")

# printing the first 10 rows
print(tourismflanders.head(10))
print(combinedAirbnb.head(10))

# printing the column names
print(tourismflanders.columns)
print(combinedAirbnb.columns)

