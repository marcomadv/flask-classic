from datetime import date,datetime
from registros_ig import app
from flask import render_template, request, redirect, flash
from registros_ig.models import *
from registros_ig.forms import MovementsForm

#Funcion para validar formulario de registro donde controlemos los input con algunos requisitos:
def validateForm(datosFormulario):
    errores = [] #crear lista para guardar errores
    hoy = date.today().isoformat() #capturo la fecha de hoy 
    if datosFormulario['date'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concept'] == "":
        errores.append("El concepto no puede estar vacio")
    if float(datosFormulario['quantity']) == 0.0 or datosFormulario['quantity'] == '':
        errores.append("El monto debe ser mayor a 0 o distinto de vacio")
    
    return errores

@app.route("/")
def index():

    registros = select_all()

    return render_template("index.html", data=registros)

@app.route("/new", methods=["GET","POST"])
def create():

    form = MovementsForm()

    if request.method == "GET":
        return render_template("create.html", dataForm=form)
    else:               #si es "post";
        
        if form.validate_on_submit:
            insert([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data]) #funcion creada insert, con los datos del formulario, separados y todos ellos dentro de corchetes, para pasarlo como una lista     
            
            flash("Movimiento registrado correctamente")
            return redirect("/")
        else:
            return render_template("create.html",dataForm=form)
            
    
@app.route("/delete/<int:id>", methods=["GET","POST"])
def remote(id):
    if request.method == "GET":
        resultado = select_by(id)
        return render_template("/delete.html", data=resultado )
    else:
        delete_by(id)
        flash("Eliminado correctamente")
        return redirect("/")
    
@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):

    form = MovementsForm()

    if request.method == "GET":
        resultado = select_by(id) #resultado de los datos del id viene como tupla
        resultado[0]#id
        resultado[1]#date
        resultado[2]#concept
        resultado[3]#monto

        form.date.data=datetime.strptime(resultado[1],"%Y-%m-%d")
        form.concept.data=resultado[2]
        form.quantity.data=resultado[3]

        return render_template("update.html",dataForm=form, idform=id)
    else:
        if form.validate_on_submit():
            #aqui ingresa el post
            update_by(id,[form.date.data.isoformat(),
                        form.concept.data,
                        form.quantity.data])
            flash("Actualizado correctamente")
            return redirect("/")
        else:
            return render_template("create.html",dataForm=form)
