import pandas as pd
import requests
import re
from hashmap import export_hashmap_to_excel

tourismflanders = pd.read_excel("Thesis_Data_Preprocessed.xlsx", sheet_name="TourismFlanders", engine="openpyxl")

def fetch_html(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

def extract_after_listing_title(html):
    if html:
        match = re.search(r'"listingTitle":"(.*?)"', html)
        return match.group(1) if match else None
    return None

tourismflanders['html_content'] = tourismflanders['website'].apply(fetch_html)
tourismflanders['filtered_html'] = tourismflanders['html_content'].apply(extract_after_listing_title)

def export_to_excel(df, filename):
    df.to_excel(filename, index=False)  # Ensure index=False to prevent unnecessary row shifts

export_to_excel(tourismflanders, "html_pages.xlsx")
