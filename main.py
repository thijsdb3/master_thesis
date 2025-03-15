import hashmap
import airbnb_preprocessing as airbnb
import tourism_flanders_preprocessing as tf

Ghent = airbnb.process_airbnb("listingsGhent.csv")
Antwerp = airbnb.process_airbnb("listingsAntwerp.csv")
toerismeflanders = tf.process_tourismflanders()


ghent_hashmap = hashmap.create_city_hashmap(Ghent, toerismeflanders)
antwerp_hashmap = hashmap.create_city_hashmap(Antwerp, toerismeflanders)

print(ghent_hashmap)
print(antwerp_hashmap)

import csv

def save_dict_to_csv(filename, data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Key", "Value"])  # Adjust based on hashmap structure
        for key, value in data.items():
            writer.writerow([key, value])

save_dict_to_csv("ghent_hashmap.csv", ghent_hashmap)
save_dict_to_csv("antwerp_hashmap.csv", antwerp_hashmap)

