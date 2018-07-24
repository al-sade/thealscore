import logging
from spotify import SpotifyHandler
from deezer import DeezerHandler


class Calculator:
    def __init__(self, artist):
        self.artist = artist
        self.final_score = {}
        self.execute()

    def execute(self):
        try:
            self.get_spotify()
        except Exception as e:
            logging.error(msg=e)

    def get_spotify(self):
        spotify = SpotifyHandler(self.artist)
        spotify_score = spotify.get_artist()
        self.final_score['spotify'] = spotify_score

    def get_deezer(self):
        deezer = DeezerHandler(self.artist)
        deezer_score = deezer.get_artist()
        self.final_score['deezer'] = deezer_score

