
import numpy as np
from geopy.distance import geodesic
import airbnb_preprocessing as airbnb
import tourism_flanders_preprocessing as tf

tourism_flanders = tf.process_tourismflanders()
inside_airbnb = airbnb.process_airbnb()

airbnb_coords = inside_airbnb[['latitude', 'longitude']].to_numpy()

