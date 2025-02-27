
import numpy as np
import airbnb_preprocessing as airbnb
import tourism_flanders_preprocessing as tf

Ghent =  airbnb.process_airbnb("listingsGhent.csv")
Antwerp = airbnb.process_airbnb("listingsAntwerp.csv")

print("this is the ghent airbnb ""\n" ,Ghent)
print("this is the antwerp airbnb""\n",Antwerp)
GHENT_CENTER = (51.05, 3.72)
ANTWERP_CENTER = (51.22, 4.40)

ghent_map = airbnb.plot_airbnb_map("Ghent", Ghent, *GHENT_CENTER)
antwerp_map = airbnb.plot_airbnb_map("Antwerp", Antwerp, *ANTWERP_CENTER)


# Save the maps as HTML files
ghent_map.save("ghent_airbnb_map.html")
antwerp_map.save("antwerp_airbnb_map.html")

print("Maps saved as 'ghent_airbnb_map.html' and 'antwerp_airbnb_map.html'.")