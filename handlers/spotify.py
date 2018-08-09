import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from config import client_secret, client_id, username, redirect_uri


class SpotifyHandler:
    def __init__(self, artist):
        self.client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.artist = artist

    def get_artist(self):
        sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        result = sp.search(q='artist:' + self.artist, type='artist')

        try:
            return result['artists']['items'][0]
        except Exception as e:
            return False