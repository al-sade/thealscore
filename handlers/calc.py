import logging
from spotify import SpotifyHandler
from deezer import DeezerHandler
import random

class Calculator:
    def __init__(self, artist):
        print('Calc instance created!')
        self.artist = artist

    def get_summary(self):
        summary = {}
        try:
            summary['spotify'] = self.get_spotify()
            summary['deezer'] = self.get_deezer()
            return summary

        except Exception as e:
            logging.error(msg=e)
            return false

    def get_spotify(self):
        try:
            spotify = SpotifyHandler(self.artist)
            spotify_score = spotify.get_artist()
            spotify_albums = spotify.get_albums()
            related_artists = spotify.get_artist_related_artists()
            top_tracks = spotify.get_artist_top_tracks()
            return {
                'spotify_score': spotify_score,
                'spotify_albums': spotify_albums,
                'related_artists': related_artists,
                'top_tracks': top_tracks
            }
        except Exception as e:
            logging.error(msg=e)
            return false


    def get_deezer(self):
        try:
            deezer = DeezerHandler(self.artist)
            deezer_score = deezer.get_artist()
            return deezer_score

        except Exception as e:
            logging.error(msg=e)
        return false

