from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contacto import Contact
from utils.db import db

contactos=Blueprint("contacto",__name__)

#AL INICIAR EL PROGRAMA MUESTRA LA VENTANA INICIAL 'index.html'
@contactos.route("/")
def index():    
    contactos = Contact.query.all()     
    return render_template('index.html', contactos=contactos)


#AL PRESIONARSE EL BOTÓN GUARDAR SE EJECUTA EL MÉTODO POST
@contactos.route('/new', methods=['POST'])
def add_contact():
    if request.method == 'POST':

        #RECOGE LA DATA INGRESADA EN EL FORMULARIO DE INGRESO DE USUARIO Y LA GUARDA EN LA VARIABLES:
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']

        #CREA UN NUEVO CONTACTO (USUARIO) CON LOS DATOS OBTENIDOS
        new_contact = Contact(fullname, email, phone)

        #GUARDA EL USUARIO EN LA BASE DE DATOS
        db.session.add(new_contact)

        #MANDA UN COMMIT A LA BASE DE DATOS CON LA ACTUALIZACIÓN
        db.session.commit()

        #MUESTRA EN PANTALLA QUE EL CONTACTO DE AGREGÓ CORRECTAMENTE
        flash('Contact added successfully!')

        #REDIRIGE A CONTACTO.INDEX (index.html)
        return redirect(url_for('contacto.index'))


#AL PRESIONARSE EL BOTÓN EDITAR SE EJECUTA:
@contactos.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    #SE OBTIENE EL CONTACTO(USUARIO) POR MEDIO DEL ID
    contact = Contact.query.get(id)

    #SI SE ENCUENTRA EN EL MÉTODO POST (LUEGO DE EDITAR)
    if request.method == "POST":
        #EN LA PÁGINA AL MOMENTO DE GUARDAS SE OBTIENE LOS NUEVOS CAMPOS
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        #SE ACTUALIZA EN LA BASE DE DATOS
        db.session.commit()

        #MANDA UN MENSAJE DE QUE SE HA ACTUALIZADO CORRECTAMENTE
        flash('Contact updated successfully!')

        #SE REDIRIGE A contacto.index(index.html)
        return redirect(url_for('contacto.index'))
    
    #SI SE ENCUENTRA EN EL MÉTODO GET (ANTES DE EDITAR: AL PRESIONAR EL BOTÓN)
    #SE REDIRIGE A LA PÁGINA update.html CON LOS DATOS DEL CONTACTO OBTENIDO
    return render_template("update.html", contact=contact)


#CUANDO SE PRESIONA EL BOTÓN ELIMINAR
@contactos.route("/delete/<id>", methods=["GET"])
def delete(id):
    #SE OBTIENE EL CONTACTO(USUARIO) POR MEDIO DE SU ID
    contact = Contact.query.get(id)

    #SE ELIMINA EL CONTACTO
    db.session.delete(contact)

    #SE MANDA LA ACTUALIZACIÓN A LA BASE DE DATOS
    db.session.commit()

    #MUESTRA EL MENSAJE DE QUE EL CONTACO HA SIDO ELIMINADO
    flash('Contact deleted successfully!')

    #REDIRIGE A LA PÁGINA contacto.index(index.html)
    return redirect(url_for('contacto.index'))



#AL PRESIONAR EL BOTÓN ABOUT (UBICADO EN EL NAVBAR)
@contactos.route("/about")
def about():
    #REDIRIGE A LA PÁGINA about.html
    return render_template("about.html")
