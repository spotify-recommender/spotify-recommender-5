from flask import Flask, render_template, request
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .functions import get_track_info, get_track_feats
from .models import knn, graph
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns
import pandas as pd


def create_app():
    # Inializes the app
    APP = Flask(__name__)

    # Connecting to Spotifys API
    API_KEY = os.getenv("CLIENT_ID")
    SECRET_KEY = os.getenv("CLIENT_ID_SECRET")
    CLIENT_MANAGER = SpotifyClientCredentials(client_id=API_KEY, client_secret=SECRET_KEY)
    SPOTIFY = spotipy.Spotify(client_credentials_manager=CLIENT_MANAGER)

    
    
    @APP.route('/', methods=['GET', "POST"])
    def root():
        '''Home/Base Page'''

        # This is the song name given on the webapp
        name = request.form.get('name')
        error = False
        # Simple Try and Except code to keep things smooth
        try:
            # Getting the track ID number
            track_id = SPOTIFY.search(name, type='track', limit=1)['tracks']['items'][0]['id']
            #  Getting track information from function
            results = get_track_info(track_id)

            # Using function that gets features
            track = get_track_feats(track_id)
            
            # getting all the features into a list for the model
            list_of_track_feats = []
            for x in track:
                 feat = track[x]
                 list_of_track_feats.append(feat)

            # Using the knn function for the models.py
            # to get back a list of song ids
            ids = knn(list_of_track_feats)

            graph(ids, list_of_track_feats)
            # If statement so if the search id is equal
            # to the first id in the list. it will skip the first
            # song and use the last 10.
            if track_id == ids[0]:
                ids = ids[1:]
            else:
                ids = ids[0:10]
            # For loop to get song information for the predicted songs
            pred_songs_info_list = []
            for song in ids:
                song_info = get_track_info(song)
                pred_songs_info_list.append(song_info)
            
            # returning the search to be True(Success)
            search=True
        
        except:
            # Throwing errors and settings everything to raise errors
            error = True
            search = False
            results = False
            pred_songs_info_list = False


        # Returning everything back to the html file to format
        return render_template('index.html',
            error = error,
            search = search,
            sres = results,
            recommended = pred_songs_info_list
        )
    
    @APP.route('/About-The-Team', methods=['GET', "POST"])
    def about_the_team():
        '''Page that gives the teams information'''

        return render_template('about-the-team.html')

    return APP
