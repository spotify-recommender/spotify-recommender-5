import pickle
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import seaborn as sns
import matplotlib.pyplot as plt
from .functions import normalize

API_KEY = os.getenv("CLIENT_ID")
SECRET_KEY = os.getenv("CLIENT_ID_SECRET")
CLIENT_MANAGER = SpotifyClientCredentials(client_id=API_KEY, client_secret=SECRET_KEY)
SPOTIFY = spotipy.Spotify(client_credentials_manager=CLIENT_MANAGER)

def knn(list_of_feats):
    # Loading in the mapping data CSV
    mapping = pd.read_csv("spotify/song_mapping.csv")
    # Loading in the model using pickle
    knn = pickle.load(open("spotify/norm_knn_classless", "rb"))
    # using the normalize fuction built by sam and christine
    norm_feats = normalize(list_of_feats)
    # running the normalized features with the model
    knn_ind = knn.kneighbors([norm_feats], return_distance=False)
    #  Getting the first list of 11 songs closet to the song given
    id_df = mapping.iloc[knn_ind.tolist()[0]]
    # Turning id_df (A df into a list)
    ids = id_df['id'].tolist()
    return ids


def graph(list_of_ids, list_of_feats):
    model = pickle.load(open("ordinary_knn", "rb"))
    distance, neighbors_indexes = model.kneighbors([list_of_feats])
    if distance == []:
        return []
    # prepare output file for suggested songs
    suggest_songs = []
    for song_id in list_of_ids:
        name = SPOTIFY.track(song_id)['name']
        suggest_songs.append(name)

    output = pd.DataFrame(
        {'name': suggest_songs,
        'distance': list(distance[0])})

    fig, ax = plt.subplots(figsize=(8,8))
    ax = sns.set_theme(style='darkgrid')
    snsf = sns.catplot(x='distance', y='name', data=output)
    snsf.figure.savefig('spotify/static/distance.png')