from flask_restful import Resource
from flask import request
import xmltodict
from sqlalchemy import func

from models.pokemon import Pokemon, PokemonType


class PokemonResource(Resource):

    def post(self):
        response = {"Pokemons": []}
        try:
            data = xmltodict.parse(request.data)
            pokemon = Pokemon.query.filter(Pokemon.id == data['Request']['Pokemons']['id']).one_or_none()
            response['Pokemons'].append(pokemon.toJson())
            if pokemon is None:
                raise Exception("No pokemon found with the given id")
        except Exception as e:
            error_msg = str(e)
            error_msg = "The required data is missing: {}".format(e) if isinstance(e, KeyError) else str(e)
            return {"Error": error_msg}, 400
        return response


class PokemonSearchResource(Resource):

    def post(self):
        response = {}
        try:
            data = xmltodict.parse(request.data)
            pokemon = Pokemon.query
            if data.get('Request', None) and data['Request'].get('Search', None):
                search = data['Request'].get('Search', None)
                if search.get('Type', None):
                    pokemon = pokemon.join(Pokemon.types).filter(Pokemon.types.any(func.lower(PokemonType.p_type) == func.lower(search.get('Type'))))
                if search.get('Name', None):
                    pokemon = pokemon.filter(Pokemon.name.contains(search.get('Name')))
            pokemons = [p.toJson() for p in pokemon.all()]
            response['Pokemons'] = pokemons
            if pokemons is None:
                return response, 400
        except Exception as e:
            error_msg = str(e)
            error_msg = "The required data is missing: {}".format(e) if isinstance(e, KeyError) else str(e)
            return {"Error": error_msg}, 400
        return response
