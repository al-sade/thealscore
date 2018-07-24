
class DeezerHandler:
    def __init__(self, artist):
        self.client = deezer.Client()
        self.artist = artist

    def get_artist(self):
        result = True  # tmp placeholder
        return result
