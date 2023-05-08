from datetime import date
from registros_ig import app
from flask import render_template, request, redirect
from registros_ig.models import *

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

    if request.method == "GET":
        return render_template("create.html", dataForm=None) #pasamos dataform para que no de error pero sin valores
    else:               #si es "post";
        errores = validateForm(request.form)
        if errores:
            return render_template("create.html", msgError = errores, dataForm=request.form) #que no borre los datos si hay error
        else:
            insert([request.form['date'],
                    request.form['concept'],
                    request.form['quantity']
                    ]
                    ) #funcion creada insert, con los datos del formulario, separados y todos ellos dentro de corchetes, para pasarlo como una lista
            
        return redirect("/")
    
@app.route("/delete/<int:id>", methods=["GET","POST"])
def remote(id):
    if request.method == "GET":
        resultado = select_by(id)
        return render_template("/delete.html", data=resultado )
    else:
        delete_by(id)
        
        return redirect("/")
