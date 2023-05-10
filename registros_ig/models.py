from registros_ig.conexion import *

def select_all():
   
    conectar = Conexion("select * from movements order by date DESC")
    
    filas = conectar.res.fetchall() #(1,2023-05-05,sueldo,1600)
    columnas = conectar.res.description #columnas(id,0,0,0,0,0)

    #objetivo crear una lista de diccionario con filas y columnas
    lista_diccionario = []
    
    for f in filas:
        diccionario = {}
        posicion = 0
        for c in columnas:
            diccionario[c[0]]= f[posicion]
            posicion += 1
        lista_diccionario.append(diccionario)

    conectar.con.close() #cerramos la conexion 
    return lista_diccionario

def insert(registroForm):
    conectarInsert = Conexion("INSERT INTO movements(date,concept,quantity) VALUES(?,?,?)", registroForm)
    conectarInsert.con.commit() #validacion de registros
    conectarInsert.con.close() #cierre de conexion

def select_by(id): #funcion para seleccionar datos de un id especifico
    conectSelectBy = Conexion(f"SELECT * FROM movements WHERE id={id}")
    resultado = conectSelectBy.res.fetchall()
    conectSelectBy.con.close()

    return resultado[0]  #[0]-De este modo nos devuelve el registro del id como una lista, no como lista de tuplas.

def delete_by(id): #funcion para borrar un id especifico
    conectDeleteBy = Conexion(f"DELETE FROM movements WHERE id={id}")
    conectDeleteBy.con.commit()
    conectDeleteBy.con.close()

def update_by(id,registro):
    conectUpdateBy = Conexion(f"UPDATE movements SET date = ?, concept=?, quantity = ? WHERE id ={id};",registro)
    conectUpdateBy.con.commit()
    conectUpdateBy.con.close()