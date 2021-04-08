from flask import abort
from flask.json import jsonify
from flask_restful import Resource
from sqlalchemy.orm.exc import NoResultFound
from app import api,db

from models.ejemplo import Ejemplo, EjemploSchema
ejemplo_schema = EjemploSchema()
ejemplo_schema_many = EjemploSchema(many=True)

class ExampleAPI(Resource):
    def get(self,id=None):
        if id is not None:
            try:
                ejem = Ejemplo.query.get(id)
                return jsonify(ejemplo_schema.dump(ejem))
            except NoResultFound:
                abort(404)
        else:
            ejem = Ejemplo.query.all()
            return jsonify(ejemplo_schema_many.dump(ejem))
    
    def post(self,nombre):
        temp=Ejemplo(str(nombre))
        temp.save()

api.add_resource(ExampleAPI, '/api',endpoint = 'todos')
api.add_resource(ExampleAPI, '/api/<int:id>',endpoint = 'uno')

