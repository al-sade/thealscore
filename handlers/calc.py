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
        # return random.randint(1,100)
        try:
            spotify = SpotifyHandler(self.artist)
            spotify_score = spotify.get_artist()
            return spotify_score

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

