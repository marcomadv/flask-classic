import sqlite3    # importamos sqlite
from registros_ig import ORIGIN_DATA #importamos para que nos funcionen las variables de ruta creadas en init (ORIGIN_DATA)

def select_all():
    con = sqlite3.connect(ORIGIN_DATA) # conectar con base de datos
    cur = con.cursor() #cursor para poder ejecutar las querys

    res = cur.execute("select * from movements;")  #query o peticion a la base de datos

    filas = res.fetchall() #(1,2023-05-05,sueldo,1600)
    columnas = res.description #columnas(id,0,0,0,0,0)

    #objetivo crear una lista de diccionario con filas y columnas
    lista_diccionario = []
    
    for f in filas:
        diccionario = {}
        posicion = 0
        for c in columnas:
            diccionario[c[0]]= f[posicion]
            posicion += 1
        lista_diccionario.append(diccionario)

    con.close() #cerramos la conexion 
    return lista_diccionario

def insert(registroForm):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute("INSERT INTO movements(date,concept,quantity) VALUES(?,?,?)", registroForm) #hacer insert en base datos de los datos añadidos en formulario
    
    con.commit() #validacion de registros
    con.close() #cierre de conexion

def select_by(id): #funcion para seleccionar datos de un id especifico
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute(f"SELECT * FROM movements WHERE id={id}")
    resultado = res.fetchall()
    con.close()

    return resultado[0]  #[0]-De este modo nos devuelve el registro del id como una lista, no como lista de tuplas.

def delete_by(id): #funcion para borrar un id especifico
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    cur.execute(f"DELETE FROM movements WHERE id={id}")

    con.commit()
    con.close()