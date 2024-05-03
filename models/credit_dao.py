import sqlite3
import math
import os
from tkinter import messagebox
from docxtpl import DocxTemplate


import processes
from processes.str_and_date_processes import process_data_str_to_date,processes_data_date,convert_to_month
from processes.math_processes import check_integer

from .conexion_db import ConexionDB
from .models import Expiration_Dates

def search_judicial_credits(account):
    """_summary_

    Args:
        account (_type_): _description_
    """  
    try:  
        conexion=ConexionDB()
        sql=f""" SELECT id_ju from judiciales WHERE cuenta={account} and estado=1"""
        conexion.cursor.execute(sql)
        data=conexion.cursor.fetchall()
        conexion.close()
        return data 
    except TypeError:
         return None

def search_account_credits_info(account):
    """_summary_:return list of credits 

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

def search_product(credit):
    conexion=ConexionDB()
    sql=f""" SELECT producto from creditos where credito={credit}"""   
    conexion.cursor.execute(sql)
    product=conexion.cursor.fetchall()
    conexion.close() 
    product=list(product)
    product=list(product[0])
    product=product[0]
    return product
     
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
               
def interest_calculation(today,expiration_date,amount,mora):
     delta_days=today-expiration_date
     delta_days=delta_days.days
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
    sql=sql_1=f"""UPDATE fechas_pagos SET estado =0  where credito={credit}"""
    conexion.cursor.execute(sql)
    sql_1=f"""UPDATE creditos SET estado =0  where credito={credit}"""
    conexion.cursor.execute(sql_1)
    conexion.close()

def delete_guardator(credit):
    conexion=ConexionDB()
    sql=f""" DELETE FROM garantes WHERE credito={credit}"""
    conexion.cursor.execute(sql)
    conexion.close()


def write_new_judicial_credit(Judicial):
        conexion=ConexionDB()
        sql=f"""INSERT INTO judiciales (cuenta,monto,fecha,estado)
        VALUES ('{Judicial.account}','{Judicial.amount}','{Judicial.date}','{Judicial.state}')
    """   
        conexion.cursor.execute(sql)
        sql_1=f"""SELECT MAX(id_ju) FROM judiciales;"""
        conexion.cursor.execute(sql_1)
        max_id=conexion.cursor.fetchall()
        conexion.close()
        max_id=list(max_id)
        max_id=list(max_id[0])
        max_id=max_id[0]
        return max_id

def write_new_judicial_info(new_info):
        conexion=ConexionDB()
        sql=f"""INSERT INTO judicial_info (nombre,direccion,telefono,producto,credito_judicial)
        VALUES ('{new_info.name}','{new_info.address}','{new_info.phone}','{new_info.product}','{new_info.judicial_credit}')
    """   
       
        conexion.cursor.execute(sql)
        conexion.close()

def search_all_credit_info(credit):
    """_summary_:retunr list have fecha_id,fecha,monto,estado,acuenta

    Args:
        credit (_type_): _description_

    Returns:
        _type_: _description_
    """    
    conexion=ConexionDB()
    sql=f"""SELECT fecha_id,fecha,cuota,monto,acuenta,estado FROM fechas_pagos where credito={credit} and estado='Por Pagar'"""
    conexion.cursor.execute(sql)
    credit=conexion.cursor.fetchall()
    conexion.close()
    t=0
    for i in credit:
         credit[t]=list(i)
         t+=1
    return credit

def update_quote(money,state,credit,quote):
    conexion=ConexionDB()
    sql=f"""UPDATE fechas_pagos SET estado ='{state}' , acuenta = acuenta+{money} where credito={credit} and cuota={quote};"""
    conexion.cursor.execute(sql)
    credit=conexion.cursor.fetchall()
    conexion.close()
     
def writte_new_pay(Pay):
        conexion=ConexionDB()
        sql=f"""INSERT INTO pagos (fecha_pago,datos,cuenta)
        VALUES ('{Pay.date}','{Pay.data}','{Pay.account}')
    """ 
        conexion.cursor.execute(sql)
        conexion.close()


def generate_payment_receipt(today,diccionario_pagos,dni,nombre,cuenta,flag):
     keys = list(diccionario_pagos.keys())
     
     for keys in diccionario_pagos:
          valor=diccionario_pagos[keys]
          t=0
          for i in valor:
               i[1]=str(i[1])
               i[1]=i[1].ljust(10)
               valor[t][1]=i[1]
               if i[6]==0:
                    valor[t][4]="A cuenta"
                    valor[t][4]=valor[t][4].ljust(16)
               if i[6]==1: 
                    valor[t][4]="Cuota Cancelada"
                    valor[t][4]=valor[t][4].ljust(16)
               t=t+1
          diccionario_pagos[keys]=valor  
     template_location=os.path.join(os.path.abspath(os.getcwd()),"templates/pay_templates/")
     archive_location=os.path.join(template_location, 'Pay.docx')  
     
     white_model= DocxTemplate(archive_location)
     pay_date=processes_data_date(today)
     partes_fecha = pay_date.split("-")
     mounth=convert_to_month(check_integer(partes_fecha[1]))

     
     context={
          
          'hoy':partes_fecha[0],
           'diccionario':diccionario_pagos,
           'mes':mounth,
           'ano':partes_fecha[2],
        'nombre':nombre,
          'dni': dni,
          'claves_pagos':list(diccionario_pagos.keys()),
          'cuenta':cuenta
        
     }
     white_model.render(context)
     rute_folder=os.path.join("pagos",f"{partes_fecha[1]}.{partes_fecha[2]}")
     if os.path.exists(rute_folder):
        pass
     else:
        os.mkdir(rute_folder)
     rute_save=os.path.join(os.path.abspath(os.getcwd()),rute_folder)
     archive=""+"Recibo-"+nombre+"-"+str(pay_date)+"_cuenta_"+str(cuenta)+".doc"
     archive_name=os.path.join(rute_save,archive)
     white_model.save(archive_name)
     rute=os.path.join(os.path.abspath(os.getcwd()),"pagos")
     rute_archive=os.path.join(rute,f"{partes_fecha[1]}.{partes_fecha[2]}")
     if flag:
        try:
            os.startfile(rute_save,"print")
        except:
             messagebox.showerror("No se puede imprimir el archivo",f"No se pudo imprimir el recibo, el archivo se encuentra en la ruta {rute_archive}")
     else:
          messagebox.showinfo("Se Guardo el archivo",f"el archivo se guardo en \n {rute_archive}")
    