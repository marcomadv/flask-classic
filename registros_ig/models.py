import sqlite3    # importamos sqlite

def select_all():
    con = sqlite3.connect("data/movimientos.sqlite") # conectar con base de datos
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

    return lista_diccionario
    
