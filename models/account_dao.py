import sqlite3
from tkinter import messagebox

from .conexion_db import ConexionDB


def search_name_account(valor1,valor2):
    """_summary_:searches for accounts with names similar to the string entered in the database

    Args:
        valor1 (_type_): _description_
        valor2 (_type_): _description_

    Returns:
        _type_: _description_
    """ 
    try:      
        conexion=ConexionDB()
        sql=f""" SELECT dni,cuenta,nombre,contacto_direccion from cuentas WHERE {valor1} like '%{valor2}%'"""
        conexion.cursor.execute(sql)
        data=conexion.cursor.fetchall()
        conexion.close()
        return data 
    except sqlite3.OperationalError:
            messagebox.showerror("No se pudo acceder a la base de datos","No se ingresar a la base de datos","La base de datos esta siendo ocupada o esta dañada, intente más tarde")
            return ""

def search_dni_account(dni):
    """_summary_: Check if the D.N.I. entered exists in the database

    Args:
        dni (_type_): _description_

    Returns:
        _type_: _description_
    """    
    try:     
        conexion=ConexionDB()
        sql=f""" SELECT cuenta from cuentas WHERE dni={dni}"""   
        conexion.cursor.execute(sql)
        account=conexion.cursor.fetchone()
        conexion.close()
        account=list(account)
        account=account[0]
        return account
    except TypeError:
         return None
    except sqlite3.OperationalError:
            messagebox.showerror("No se pudo acceder a la base de datos","No se ingresar a la base de datos","La base de datos esta siendo ocupada o esta dañada, intente más tarde")
            return False
    
def max_account():
    """_summary_:find the largest account number

    Returns:
        _type_: _description_
    """       
    conexion=ConexionDB()
    sql=f""" SELECT max(cuenta+1) from cuentas"""   
    conexion.cursor.execute(sql)
    highest_account_number=conexion.cursor.fetchall()
    conexion.close() 
    highest_account_number=list(highest_account_number[0])
    return highest_account_number[0]

def save_new_account(New_Account):
    """_summary_: Save the new account

    Args:
        New_Account (_type_): _description_
    """    
    try:
        
        conexion=ConexionDB()
        sql=f"""INSERT INTO cuentas (cuenta,nombre,dni,contacto_telefono,contacto_direccion,direccion_trabajo,funcion)
        VALUES ('{New_Account.account_number}','{New_Account.name}','{New_Account.dni}','{New_Account.adress}','{New_Account.phone}','{New_Account.work_adress}','{New_Account.job}')
    """   
        conexion.cursor.execute(sql)
        conexion.close()
    except sqlite3.OperationalError:
           messagebox.showerror("No se pudo acceder a la base de datos","No se ingresar a la base de datos","La base de datos esta siendo ocupada o esta dañada, intente más tarde")

def check_account(cuenta):
    """_summary_: Check if the account exists

    Args:
        cuenta (_type_): _description_

    Returns:
        _type_: _description_
    """    
    try:
        conexion=ConexionDB()
        sql=f""" SELECT cuenta from cuentas WHERE cuenta={cuenta}"""   
        conexion.cursor.execute(sql)
        data=conexion.cursor.fetchone()
        conexion.close()
        data=list(data)
        data=data[0]
        return data
    except sqlite3.OperationalError:
        messagebox.showerror("No se pudo acceder a la base de datos","No se ingresar a la base de datos","La base de datos esta siendo ocupada o esta dañada, intente más tarde")
        return None
    except TypeError:
        return None
    
def search_data_account(cuenta):
        """_summary_: Search for account details

    Args:
        cuenta (_type_): _description_

    Returns:
        _type_: _description_
    """ 
        try:       
            conexion=ConexionDB()
            sql=f""" SELECT nombre,dni,contacto_telefono,contacto_direccion from cuentas WHERE cuenta={cuenta}"""   
            conexion.cursor.execute(sql)
            data=conexion.cursor.fetchone()
            conexion.close()
            data=list(data)
            return data
        except sqlite3.OperationalError:
            messagebox.showerror("No se pudo acceder a la base de datos","No se ingresar a la base de datos","La base de datos esta siendo ocupada o esta dañada, intente más tarde")
            return None
        
def update_data(account,field,new_value):
    """_summary_: update account data

    Args:
        account (_type_): _description_
        field (_type_): _description_
        new_value (_type_): _description_
    """    
    try:
        conexion=ConexionDB()
        sql=f""" update cuentas set {field}='{new_value}' where cuenta={account}
    """
        conexion.cursor.execute(sql)
        conexion.close()
    except sqlite3.OperationalError:
        messagebox.showerror("No se pudo acceder a la base de datos","No se ingresar a la base de datos","La base de datos esta siendo ocupada o esta dañada, intente más tarde")
        