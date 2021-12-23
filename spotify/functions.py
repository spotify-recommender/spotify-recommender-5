import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns
import pandas as pd


API_KEY = os.getenv("CLIENT_ID")
SECRET_KEY = os.getenv("CLIENT_ID_SECRET")
CLIENT_MANAGER = SpotifyClientCredentials(client_id=API_KEY, client_secret=SECRET_KEY)
SPOTIFY = spotipy.Spotify(client_credentials_manager=CLIENT_MANAGER)


def get_track_info(id):
    ''' Function takes in the track id and returns a dictionary
    of track information''' 

    # Gathering track information
    track = SPOTIFY.track(id)

    # Saving the song name, artist, and url to a dict
    information = {
        'song' : track['name'],
        'artist' : track['album']['artists'][0]['name'],
        'url': track['external_urls']['spotify'],
        'image': track['album']['images'][2]['url'],
        'preview_url': track['preview_url']
    }

    return information


def get_track_feats(id):
    """ This function will take a tracks id and return
    its features dropping information that is not needed."""
        
    features = SPOTIFY.audio_features(id)[0]

    # Use this for the final model
    drops_these_features = ['type', 'id',
        'uri', 'track_href', 'analysis_url','time_signature','key','mode']


    for drop in drops_these_features:
        features.pop(drop)

    return features


def normalize(data):
    '''Function from Sam and Christine'''
    newdata = []
    for i in range(len(data)):
        if i == 2:
            newdata.append(max(0, (min(data[i], 7.234) - (-60.0)) / (7.234 - (-60.0))))
        elif i == 8:
            newdata.append(
                max(
                    0,
                    (min(data[i], 248.93400000000003) - 0.0)
                    / (248.93400000000003 - 0.0),
                )
            )
        elif i == 9:
            newdata.append(max(0, (min(data[i], 6061090) - 1000) / (6061090 - 1000)))
        else:
            newdata.append(data[i])
    return newdata
