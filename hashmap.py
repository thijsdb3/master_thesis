
import numpy as np
import airbnb_preprocessing as airbnb
import tourism_flanders_preprocessing as tf



GHENT_BOUNDS = (51.0, 51.2, 3.6, 3.8)  # Example bounds
ANTWERP_BOUNDS = (51.1, 51.3, 4.3, 4.5)  # Example bounds

# Filter listings for each city
ghent_airbnb = airbnb.filter_airbnb_by_city("Ghent", *GHENT_BOUNDS)
antwerp_airbnb = airbnb.filter_airbnb_by_city("Antwerp", *ANTWERP_BOUNDS)

print("this is the ghent airbnb ""\n" ,ghent_airbnb)
print("this is the antwerp airbnb""\n",antwerp_airbnb)
GHENT_CENTER = (51.05, 3.72)
ANTWERP_CENTER = (51.22, 4.40)

ghent_map = airbnb.plot_airbnb_map("Ghent", ghent_airbnb, *GHENT_CENTER)
antwerp_map = airbnb.plot_airbnb_map("Antwerp", antwerp_airbnb, *ANTWERP_CENTER)


# Save the maps as HTML files
ghent_map.save("ghent_airbnb_map.html")
antwerp_map.save("antwerp_airbnb_map.html")

print("Maps saved as 'ghent_airbnb_map.html' and 'antwerp_airbnb_map.html'.")