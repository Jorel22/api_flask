import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)


app.config.from_json('../config.json')
db = SQLAlchemy(app)
api = Api(app) 
ma = Marshmallow(app)


from api import example 

# RUTAS ESTATICAS
@app.route("/") 
def index():
    return "hola CRUD"


if __name__ == "__main__":
    app.run(debug=True)
