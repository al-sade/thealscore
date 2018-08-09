import requests
import json

class DeezerHandler:
    def __init__(self, artist):
        self.artist = artist
        self.get_artist()

    def get_artist(self):
        artist_id = self.get_artist_id()
        endpoint = 'https://api.deezer.com/artist/{}'.format(artist_id)
        result = requests.get(endpoint)
        return json.loads(result.text)

    def get_artist_id(self):
        endpoint = 'https://api.deezer.com/search?q=artist:"{}"'.format(self.artist)
        result = requests.get(endpoint)

        try:
            temp_data = json.loads(result.text)['data']
            artist_id = temp_data[0]['artist']['id']
            return artist_id
        except Exception as e:
            logging.error('Cant get artist ID / Data')
            return False

    def calc_score(self):
        pass
