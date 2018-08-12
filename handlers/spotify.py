import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from config import client_secret, client_id, username, redirect_uri


class SpotifyHandler:
    def __init__(self, artist):
        self.client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.artist = artist
        self.uri = ''

    def get_artist(self):
        sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        result = sp.search(q='artist:' + self.artist, type='artist')

        try:
            res=  result['artists']['items'][0]
            self.uri = res['uri']
            return res
        except Exception as e:
            return False

    def get_albums(self):
        sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        results = sp.artist_albums(self.uri, album_type='album')

        try:
            return results['items']
        except Exception as e:
            return False

    def get_artist_top_tracks(self):
        sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        results = sp.artist_top_tracks(self.uri)

        try:
            return results['tracks']
        except Exception as e:
            return False

    def get_artist_related_artists(self):
        sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        results = sp.artist_related_artists(self.uri)

        try:
            albums = results['artists']
            return albums
        except Exception as e:
            return False

