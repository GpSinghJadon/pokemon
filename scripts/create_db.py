import os
import json

from flask import Flask

from models import db
from models.pokemon import Pokemon, PokemonType

app = Flask(__name__)
@app.cli.command("create-db")
def create_db():
    data_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokemondata.json")
    if not os.path.exists(data_filepath):
        return "Pokemon datafile is not present"

    # Data to initialize database with
    with open(data_filepath, 'r') as f:
        pokemon_data = json.load(f)

    # Delete database file if it exists currently
    if os.path.exists("pokemon.sqlite"):
        os.remove("pokemon.sqlite")

    # Create the database
    db.create_all()

    # iterate over the pokemons and populate the database
    for pokemon in pokemon_data:
        p = Pokemon(name=pokemon.get("name"), id=pokemon.get("id"), image=pokemon.get("image"))

        # Add the types for the pokemon
        for pokemon_type in pokemon.get("types"):
            t = PokemonType.query.filter(PokemonType.p_type == pokemon_type).one_or_none()
            if t is None:
                t = PokemonType(p_type=pokemon_type)
            p.types.append(t)
        db.session.add(p)

    db.session.commit()
