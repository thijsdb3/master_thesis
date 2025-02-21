import pandas as pd
import numpy as np

def construct_full_address(row):
    address = f"{row['street']} {row['house_number']}"
    if pd.notna(row.get('boxnumber')):  # Append box number if it exists
        address += f" Box {row['boxnumber']}"
    address += f", {row['postal_code']}, Belgium"
    return address


