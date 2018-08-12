from flask import Flask, render_template, jsonify
from flask_cors import CORS
from handlers.calc import Calculator
from config import Config

app = application = Flask(__name__,
                          static_folder="./dist/static",
                          template_folder="./dist")
app.config.from_object(Config)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/artist/<name>')
def get_artist_score(name):
    summary = Calculator(name).get_summary()
    response = {
        'summary': summary
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
