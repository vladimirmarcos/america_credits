import sqlite3

from .conexion_db import ConexionDB
from .models import Expiration_Dates

def search_judicial_credits(account):
    """_summary_

    Args:
        account (_type_): _description_
    """  
    try:  
        conexion=ConexionDB()
        sql=f""" SELECT id_ju,credito from judiciales WHERE cuenta={account} and estado=1"""
        conexion.cursor.execute(sql)
        data=conexion.cursor.fetchall()
        conexion.close()
        return data 
    except TypeError:
         return None

def search_account_credits_info(account):
    """_summary_

    Args:
        account (_type_): _description_
    """
    try:
        conexion=ConexionDB()
           
        sql=f""" SELECT credito from creditos WHERE cuenta={account} and estado=1"""
        conexion.cursor.execute(sql)
        credit=conexion.cursor.fetchall()
        conexion.close()
        credit=list(credit)
        t=0
        for i in credit:
            f=list (i)
            credit[t]=i[0]
            t=t+1
        return credit
    except TypeError:
         return None
    
def search_credit_info(credit):
    """_summary_

    Args:
        credit (_type_): _description_
    """ 
    conexion=ConexionDB()
    sql=f"""SELECT MIN(fecha),fecha_id,monto,estado,acuenta FROM fechas_pagos where credito={credit} and estado='Por Pagar'"""
    conexion.cursor.execute(sql)
    credit=conexion.cursor.fetchall()
    conexion.close()
    credit=list(credit[0])
    return credit

def write_new_credit(Credit):
        """_summary_:w

    Args:
        Account (_type_): _description_
    """        
        conexion=ConexionDB()
        sql=f"""INSERT INTO creditos (cuenta,cuotas,producto,monto_financiado,fecha,estado)
        VALUES ('{Credit.account}','{Credit.fee}','{Credit.products}','{Credit.amount}','{Credit.issue_data}','{Credit.state}')
    """   
        conexion.cursor.execute(sql)
        conexion.close()

def search_maximum_credit():
    """_summary_: look for the maximum id in the credits table

    Returns:
        max_id(int): the maximum id in the credits table
    """    
    conexion=ConexionDB()
    sql=f""" SELECT max(credito) from creditos"""   
    conexion.cursor.execute(sql)
    id_credit=conexion.cursor.fetchall()
    conexion.close() 
    id_credit=list(id_credit[0])
    return id_credit[0]

def write_expiration_dates(max_id_credit,expirated_date_list,amount):
    """_summary_

    Args:
        max_id_credit (_type_): _description_
        expirated_date_list (_type_): _description_
        amount (_type_): _description_
    """    
    conexion=ConexionDB()
    t=1
    for i in expirated_date_list:
        new_expiration_date=Expiration_Dates(i[0],
                                          amount,
                                          i[1],
                                          "Por Pagar",
                                          max_id_credit,
                                          t)
        sql=f"""INSERT INTO fechas_pagos (fecha,monto,estado,acuenta,credito,cuota)
        VALUES ('{new_expiration_date.date}','{new_expiration_date.amount}','{new_expiration_date.state}','{new_expiration_date.on_account}','{new_expiration_date.credit}','{new_expiration_date.fee}')
    
        """
        conexion.cursor.execute(sql)
        t+=1
    conexion.close()   

def write_new_guardator(Guardator):
        """_summary_

    Args:
        Guardator (_type_): _description_
    """       
        conexion=ConexionDB()
        sql=f"""INSERT INTO garantes (nombre,direccion,telefono,credito)
        VALUES ('{Guardator.name}','{Guardator.address}','{Guardator.phone}','{Guardator.credit}')
    """   
        conexion.cursor.execute(sql)
        conexion.close()

 