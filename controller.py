import random
from datetime import datetime
import spotipy
import spotipy.util as util
from spotifyInfo import *


def validate(username, scope, spotipy_client_id, spotipy_client_secret, spotipy_redirect_url):

    token = util.prompt_for_user_token(username, scope, client_id = spotipy_client_id, client_secret = spotipy_client_secret, redirect_uri = spotipy_redirect_url)
    if not token:
        print("Cannot get token for ", username, "\nquitting")
        quit()
    return token

def getTrackInfo(spotify):
    current_track = spotify.currently_playing()
    track = current_track['item']
    return {
        "name" : track['name'],
        "coverUrl" : track['album']['images'][0]['url'],
        "artist" : track['album']['artists'][0]['name'],
        "album" : track['album']['name'],
        # "progress": current_track['progress_ms'],
        # "length": track['duration_ms']
    }

def handleSpotify():
    username = user
    scope = 'user-read-recently-played user-read-currently-playing user-modify-playback-state'
    
    token = validate(username, scope, client_id, client_secret, redirect_url)

    spotify = spotipy.Spotify(auth = token)
    spotify.trace = False
    
    current_track = getTrackInfo(spotify)
    print(current_track)
    return current_track
    
