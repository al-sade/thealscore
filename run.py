from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
import json

#handlers
from handlers.spotify import spotifyHandler

app = application =Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/artist/<name>')
def get_artist_score(name):
    spotify = spotifyHandler()
    spotify_score = spotify.getArtist(name)
    response = {
        'score': spotify_score
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
