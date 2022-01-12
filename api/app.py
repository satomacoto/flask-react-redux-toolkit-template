from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pokemons = {
    "bulbasaur": {
        "species": {
            "name": "bulbasaur",
        },
        "sprites": {
            "front_shiny": "https://picsum.photos/200"  # dummy image
        }
    }
}

@app.route("/api/v1/pokemon/<name>")
def pokemon(name):
    pokemon = pokemons.get(name, None)
    if pokemon:
        return jsonify(pokemon), 200
    else:
        return jsonify({}), 400

