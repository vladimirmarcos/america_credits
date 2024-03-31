from .conexion_db import ConexionDB
import sqlite3

def search_name_account(valor1,valor2):
    """_summary_:searches for accounts with names similar to the string entered in the database

    Args:
        valor1 (_type_): _description_
        valor2 (_type_): _description_

    Returns:
        _type_: _description_
    """       
    conexion=ConexionDB()
    sql=f""" SELECT dni,cuenta,nombre,contacto_direccion from cuentas WHERE {valor1} like '%{valor2}%'"""
    conexion.cursor.execute(sql)
    datos=conexion.cursor.fetchall()
    conexion.cerrar()
    return datos 