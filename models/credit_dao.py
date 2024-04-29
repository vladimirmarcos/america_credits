import sqlite3
import math

import processes
from processes.str_and_date_processes import process_data_str_to_date

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

def search_all_credit_account(account):
     """_summary_

    Args:
        account (_type_): _description_

    Returns:
        _type_: _description_
    """     
     conexion=ConexionDB()
     sql=f"""select credito,producto,monto_financiado FROM creditos WHERE cuenta={account} and estado=1"""
     conexion.cursor.execute(sql)
     list_credit=conexion.cursor.fetchall()
     conexion.close()
     if list_credit!=[]:
        t=0
        for i in list_credit:
          list_credit[t]=list(i)
          t+=1
        return list_credit
     else:
          return False

def search_info_guardator(list_credit):
     """_summary_

    Args:
        list_credit (_type_): _description_
     """     
     list_guardator=[]
     conexion=ConexionDB()
     for i in list_credit:
        sql=f"""select nombre,telefono,direccion FROM garantes WHERE credito={i[0]}"""
        conexion.cursor.execute(sql)
        list_credit=conexion.cursor.fetchone()
        list_guardator.append(list(list_credit))
     conexion.close()
     return list_guardator

def search_rest_credit(credit):
     """_summary_

    Args:
        credit (_type_): _description_

    Returns:
        _type_: _description_
    """  
     conexion=ConexionDB()
     sql=f"select fecha,monto,acuenta FROM fechas_pagos WHERE credito={credit} and estado='Por Pagar'"
     conexion.cursor.execute(sql)
     rest_credit=conexion.cursor.fetchall()
     conexion.close()
     j=0
     for i in rest_credit:
          rest_credit[j]=list(i)
          j+=1
     return rest_credit
     
def calculate_rest_of_the_credits(list_credit,today):
     rest_credit=[]
     for i in list_credit:
          auxiliary=search_rest_credit(i[0])
          total_credit=0.0
          for j in auxiliary:
               expiration_date=process_data_str_to_date(j[0])
               expiration_date=expiration_date.date()
               if expiration_date<today:
                    interests=interest_calculation(today,expiration_date,j[1])
                    rest_quote=j[1]+interests-j[2]
                    total_credit+=rest_quote
               else:
                    rest_quote=j[1]-j[2]
                    total_credit+=rest_quote
          rest_credit.append(total_credit)  
     return rest_credit
               

def interest_calculation(today,expiration_date,amount):
     delta_days=today-expiration_date
     delta_days=delta_days.days
     mora=search_mora()
     surcharges=math.ceil((((mora/30)*delta_days)/100)*amount)
     surcharges=(surcharges/10)*10
     return surcharges

def search_mora():
    """_summary_

    Returns:
        _type_: _description_
    """    
    
    conexion=ConexionDB()
    sql=f""" SELECT moratoria from mora"""   
    conexion.cursor.execute(sql)
    mora=conexion.cursor.fetchall()
    conexion.close() 
    mora=list(mora)
    mora=list(mora[0])
    mora=mora[0]
    return mora

def delete_credit(credit):
    conexion=ConexionDB()
    sql=f""" DELETE FROM creditos WHERE credito={credit}"""
    conexion.cursor.execute(sql)
    sql_1=f""" DELETE FROM fechas_pagos WHERE credito={credit}"""
    conexion.cursor.execute(sql_1)
    conexion.close()
    