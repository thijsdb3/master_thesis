import pandas as pd
from math import *
import ast
import requests
import re

tourismflanders = pd.read_excel("Final_results.xlsx", sheet_name="TourismFlanders", engine="openpyxl")
combinedAirbnb = pd.read_excel("Final_results.xlsx", sheet_name="CombinedListingsInsideAirBNB", engine="openpyxl")
print(combinedAirbnb.columns)
def fetch_html(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

def extract_after_listing_title(html):
    if html:
        match = re.search(r'"https://www.airbnb.com/rooms/(.*?)"', html)
        return match.group(1) if match else None
    return None

tourismflanders['html_content'] = tourismflanders['website'].apply(fetch_html)
tourismflanders['filtered_html'] = tourismflanders['html_content'].apply(extract_after_listing_title)
combinedAirbnb['html_content'] = combinedAirbnb['listing_url'].apply(fetch_html)
combinedAirbnb['filtered_html'] = combinedAirbnb['html_content'].apply(extract_after_listing_title)

def export_to_excel(df, filename):
    df.to_excel(filename, index=False)  # Ensure index=False to prevent unnecessary row shifts

export_to_excel(tourismflanders, "html_pages.xlsx")
export_to_excel(combinedAirbnb, "html_checker.xlsx")