from utils.db import db

#Modelo de contacto que se utilizará en todo el programa
class Contact(db.Model):
    #Tiene las mismas medidas que la base de datos
    id= db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(100))
    email=db.Column(db.String(100))
    phone=db.Column(db.String(100))
    
    def __init__(self, fullname, email, phone ):
        self.fullname = fullname
        self.email   =email
        self.phone   =phone
