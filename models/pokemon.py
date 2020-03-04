from . import db
from collections import OrderedDict

pokemon_types_table = db.Table('pokemon_type_mappings', db.Model.metadata,
    db.Column('p_id', db.Integer, db.ForeignKey('pokemons.id')),
    db.Column('t_id', db.Integer, db.ForeignKey('pokemon_types.id'))
)


class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(150))
    types = db.relationship("PokemonType", secondary=pokemon_types_table, backref='pokemons', lazy='joined')

    def toJson(self):
        return OrderedDict({
                "Pokemon": {
                    "id": self.id,
                    "Name": self.name,
                    "Types": [{"Type": x.p_type} for x in self.types]
                }
            })


class PokemonType(db.Model):
    __tablename__ = 'pokemon_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_type = db.Column(db.String(120), unique=True, nullable=False)
