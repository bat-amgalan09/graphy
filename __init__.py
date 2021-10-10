#Imports pandas package as pd
import pandas as pd
import math
from math import radians, cos, sin, asin, sqrt
from geopy.geocoders import Nominatim

def plot_data(data):
    # Stores data as DataFrame and returns the plot
    ax = pd.DataFrame(data).plot.hist()
    return ax


def locationer(latitude, longitude):
    '''Input latitude and longtidue, return closest location addressed.'''
    locc = (latitude, longitude)
    return Nominatim(user_agent="geoapiExercises").reverse(locc)[0]

def distance_lonlat(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r
'''After converting long, lat, to radian, using spherical geometry distance formulainput longtitude and latitude of two places anywhere on the earth and returns the distance in kilometers '''