import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from config import client_secret, client_id, username

class SpotifyHandler:

    def __init__(self):
        # token = util.prompt_for_user_token(username)
        self.client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    def getArtist(self, name):
        sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        results = sp.search(q='artist:' + name, type='artist')

        return results