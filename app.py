from flask import Flask
from rutas.contacto import contactos
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from utils.db import db

app = Flask(__name__)

#AGREGA A LA CONFIGURACIÓN INICIAL DE LA APP
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"]=DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#PARA NO GUARDAR CACHE
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#SQLAlchemy(app)  NO ES NECESARIO SEGÚN EL PROGRAMA
#AGREGA LO QUE FALTA DEL CÓDIGO
app.register_blueprint(contactos)