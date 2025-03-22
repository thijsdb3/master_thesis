import pandas as pd
import requests
from hashmap import export_hashmap_to_excel

tourismflanders = pd.read_excel("Thesis_Data_Preprocessed.xlsx", sheet_name="TourismFlanders", engine="openpyxl")

def fetch_html(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

print("Before:", tourismflanders.shape)
tourismflanders['html_content'] = tourismflanders['website'].apply(fetch_html)
print("After:", tourismflanders.shape)
def export_to_excel(df, filename):
    df.to_excel(filename, index=False)  # Ensure index=False to prevent unnecessary row shifts

export_to_excel(tourismflanders,"html_pages.xlsx")