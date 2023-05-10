import sqlite3
from registros_ig import ORIGIN_DATA

class Conexion:
    def __init__(self, querySql,params=[]):  #dejamos el valor params como una lista vacia por si en el query añadimos los valores de dataform en insert, si no no tiene valor, es parametro opcional
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql,params)