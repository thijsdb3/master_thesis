import pandas as pd
import folium

def process_airbnb(file_path):
    airbnb = pd.read_csv(file_path)

    # Keep only necessary columns and drop rows with missing values
    airbnb = airbnb.dropna(subset=['latitude', 'longitude', 'neighbourhood'])
    airbnb = airbnb[['id', 'name', 'latitude', 'longitude', 'neighbourhood']]

    return airbnb



def plot_airbnb_map(city_name, airbnb_data, center_lat, center_lon):
    # Create a Folium map centered at the city's coordinates
    city_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Add Airbnb listings to the map
    for _, row in airbnb_data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['name']} ({row['neighbourhood']})",
            icon=folium.Icon(color="red", icon="home")
        ).add_to(city_map)

    return city_map

