import os
from flask import Flask, make_response
from flask_restful import Api
from models import db
from dicttoxml import dicttoxml
from scripts.create_db import create_db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'pokemon.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.app = app
app.cli.add_command(create_db)

from resources.pokemon import PokemonResource, PokemonSearchResource
api.add_resource(PokemonResource, '/list')
api.add_resource(PokemonSearchResource, '/search')


@app.after_request
def after_request_func(data):
    xml_response_text = dicttoxml(data.json, custom_root='Response', attr_type= False)
    response = make_response(xml_response_text, data.status_code)
    response.headers['Content-Type'] = 'application/xml'
    return response


if __name__ == '__main__':
    app.run(debug=True)
