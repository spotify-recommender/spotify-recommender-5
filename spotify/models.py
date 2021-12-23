import pickle
import pandas as pd
from .functions import normalize

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
