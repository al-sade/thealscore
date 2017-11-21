import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


class spotifyHandler():

    def __init__(self):
        username = 'alsade1'
        # token = util.prompt_for_user_token(username)
        self.client_id = 'f2668fb37da94edabb35fca5046f6a95'
        self.client_secret = '6ce2a34ec504405b894077b1b637b974'
        self.client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)

    def getArtist(self, name):
        sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        results = sp.search(q='artist:' + name, type='artist')

        return results