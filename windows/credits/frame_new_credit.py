import tkinter as tk
from tkinter import messagebox
from  tkcalendar import DateEntry
import datetime
import math


from ..search.frame_search import FrameSearch
import processes
from processes.math_processes import check_integer,check_float
from processes.str_and_date_processes import processes_data_str,processes_data_date
import models
from models.account_dao import search_data_account
from models.credit_dao import search_judicial_credits,write_new_credit,search_maximum_credit,write_expiration_dates,write_new_guardator
from models.models import Credits,Guardator

class FrameNewCredit(FrameSearch):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.serch_field()
        self.credit_field()

    def credit_field(self):
        self.label_account=tk.Label(self,text='Cuenta',justify="right")
        self.label_account.config(font=('Arial',12,'bold'))
        self.label_account.grid(row=1,column=0,pady=10)
        
        self.label_name_account=tk.Label(self,text='Nombre\n de cuenta',justify="right")
        self.label_name_account.config(font=('Arial',12,'bold'))
        self.label_name_account.grid(row=1,column=2,pady=10)

        self.label_dni_account=tk.Label(self,text='Dni de\n cuenta',justify="right")
        self.label_dni_account.config(font=('Arial',12,'bold'))
        self.label_dni_account.grid(row=1,column=4,pady=10)
  
        self.label_dues=tk.Label(self,text='Cuotas',justify="right")
        self.label_dues.config(font=('Arial',12,'bold'))
        self.label_dues.grid(row=2,column=0,pady=10)

        self.label_amount=tk.Label(self,text='Monto \nfinanciado',justify="right")
        self.label_amount.config(font=('Arial',12,'bold'))
        self.label_amount.grid(row=2,column=2,pady=10)

        self.label_advance=tk.Label(self,text='Anticipo',justify="right")
        self.label_advance.config(font=('Arial',12,'bold'))
        self.label_advance.grid(row=2,column=4,pady=10)

        self.label_product=tk.Label(self,text='Productos',justify="right")
        self.label_product.config(font=('Arial',12,'bold'))
        self.label_product.grid(row=2,column=6,pady=10)

        self.label_first_expiration=tk.Label(self,text='Primera \nCuota',justify="right")
        self.label_first_expiration.config(font=('Arial',12,'bold'))
        self.label_first_expiration.grid(row=3,column=0,pady=10)

        self.label_second_expiration=tk.Label(self,text='Segunda \ncuota',justify="right")
        self.label_second_expiration.config(font=('Arial',12,'bold'))
        self.label_second_expiration.grid(row=3,column=2,pady=10)

        self.label_Broadcast_date=tk.Label(self,text='Fecha \nEmisión',justify="right")
        self.label_Broadcast_date.config(font=('Arial',12,'bold'))
        self.label_Broadcast_date.grid(row=3,column=4,pady=10)

        self.label_phone_guardator=tk.Label(self,text='Telefono\n Garante',justify="right")
        self.label_phone_guardator.config(font=('Arial',12,'bold'))
        self.label_phone_guardator.grid(row=4,column=0,pady=10)

        self.label_name_guarantor=tk.Label(self,text='Nombre\n Garante',justify="right")
        self.label_name_guarantor.config(font=('Arial',12,'bold'))
        self.label_name_guarantor.grid(row=4,column=2,pady=10)

        self.label_address_guarantor=tk.Label(self,text='Direccion \nGarante',justify="right")
        self.label_address_guarantor.config(font=('Arial',12,'bold'))
        self.label_address_guarantor.grid(row=4,column=4,pady=10)

        #Entrys de cada Campo

        self.my_account=tk.StringVar()
        self.entry_account=tk.Entry(self,textvariable=self.my_account)
        self.entry_account.config(font=('Arial',12),width=15)
        self.entry_account.grid(row=1,column=1,pady=10,sticky="w")
        
        self.my_account_name=tk.StringVar()
        self.entry_account_name=tk.Entry(self,textvariable=self.my_account_name)
        self.entry_account_name.config(font=('Arial',12),width=15,state='disabled')
        self.entry_account_name.grid(row=1,column=3,pady=10,sticky="w")

        self.my_account_dni=tk.StringVar()
        self.entry_account_dni=tk.Entry(self,textvariable=self.my_account_dni)
        self.entry_account_dni.config(font=('Arial',12),width=15,state='disabled')
        self.entry_account_dni.grid(row=1,column=5,pady=10,sticky="w")

        self.my_dues=tk.StringVar()
        self.entry_dues=tk.Entry(self,textvariable=self.my_dues)
        self.entry_dues.config(width=15,font=('Arial',12),state='disabled')
        self.entry_dues.grid(row=2,column=1,pady=10,sticky="w")

        self.my_amount=tk.StringVar()
        self.entry_amount=tk.Entry(self,textvariable=self.my_amount)
        self.entry_amount.config(width=15,font=('Arial',12),state='disabled')
        self.entry_amount.grid(row=2,column=3,pady=10,sticky="w")

        self.my_advance=tk.StringVar()
        self.entry_advance=tk.Entry(self,textvariable=self.my_advance)
        self.entry_advance.config(width=15,font=('Arial',12),state='disabled')
        self.entry_advance.grid(row=2,column=5,pady=10,sticky="w")

        self.my_product=tk.StringVar()
        self.entry_product=tk.Entry(self,textvariable=self.my_product)
        self.entry_product.config(width=15,font=('Arial',12),state='disabled')
        self.entry_product.grid(row=2,column=7,pady=10,sticky="w")

        self.today = datetime.datetime.now()
        self.today=self.today.date()
        self.initial_date= self.today + datetime.timedelta(days=30)
        self.cal_1=DateEntry(self,
                           width=15,
                           locale='es_ES',
                           date_pattern='y-mm-dd',
                           year=self.initial_date.year, month=self.initial_date.month, day=self.initial_date.day)
        self.cal_1.grid(row=3,column=1,pady=10,sticky="w")

        self.cal_2=DateEntry(self,
                           width=15,
                           locale='es_ES',
                           date_pattern='y-mm-dd',
                           year=self.initial_date.year, month=self.initial_date.month, day=self.initial_date.day)
        self.cal_2.grid(row=3,column=3,pady=10,sticky="w")

        self.cal_3=DateEntry(self,
                           width=15,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_3.grid(row=3,column=5,pady=10,sticky="w")

        self.my_phone_guardator=tk.StringVar()
        self.entry_phone_guardator=tk.Entry(self,textvariable=self.my_phone_guardator,justify="left")
        self.entry_phone_guardator.config(width=15,font=('Arial',12),state='disabled')
        self.entry_phone_guardator.grid(row=4,column=1,pady=10,sticky="w")

        self.my_name_guardator=tk.StringVar()
        self.entry_name_guardator=tk.Entry(self,textvariable=self.my_name_guardator)
        self.entry_name_guardator.config(width=15,font=('Arial',12),state='disabled')
        self.entry_name_guardator.grid(row=4,column=3,pady=10,sticky="w")

        self.my_address_guardator=tk.StringVar()
        self.entry_address_guardator=tk.Entry(self,textvariable=self.my_address_guardator)
        self.entry_address_guardator.config(width=15,font=('Arial',12),state='disabled')
        self.entry_address_guardator.grid(row=4,column=5,pady=10,sticky="w")
        self.entry_account.bind ("<Return>",self.search_account)
        self._frame = None  
        
    

    def verify_account_data(self):
        data=search_data_account(self.account)
        self.name=data[0]
        self.dni=data[1]
        self.address=data[3]
        """
        messege=f"sus creditos activos son \n"
        credits_list=search_account_credits_info(self.account)
        if len(credits_list) >= 4:
            credits_list = credits_list[-3:]
        for i in credits_list:
            info=search_credit_info(i)
            qualification=self.qualification(info[0])
            messege=messege+f"el crédito {i} con calificación {qualification}\n"
        """    
        ask= messagebox.askyesno("Consulta", f"El cliente asociado al número {self.account} es {self.name}, su D.N.I. es {self.dni} y su dirección es {self.address} ")
        if ask:
             judicial_credits=search_judicial_credits(self.account)
             if judicial_credits==None or judicial_credits==[]:
                self.disenable_change_field()
                self.enable_change_fields()
             else:
                 messagebox.showerror("Error",f"La cuenta {self.account} no se le puede generar credito debido a que tiene creditos en judiciales")
                 
    
    def enable_change_fields(self):
        self.my_account_name.set(self.name)
        self.my_account_dni.set(self.dni)
        self.entry_dues.config(state="normal")
        self.entry_amount.config(state="normal")
        self.entry_advance.config(state="normal")
        self.entry_product.config(state="normal")
        self.entry_phone_guardator.config(state="normal")
        self.entry_address_guardator.config(state="normal")
        self.entry_name_guardator.config(state="normal")
        self.entry_dues.focus()

        self.entry_dues.bind ("<Return>",self.save_credit_data)
        self.entry_amount.bind ("<Return>",self.save_credit_data)
        self.entry_advance.bind ("<Return>",self.save_credit_data)
        self.entry_product.bind ("<Return>",self.save_credit_data)
        self.entry_phone_guardator.bind ("<Return>",self.save_credit_data)
        self.entry_name_guardator.bind ("<Return>",self.save_credit_data)
        self.entry_address_guardator.bind ("<Return>",self.save_credit_data)

    def disenable_change_field(self):
        self.disable(self.entry_dues,self.my_dues)
        self.disable(self.entry_amount,self.my_amount)
        self.disable(self.entry_advance,self.my_advance)
        self.disable(self.entry_product,self.my_product)
        self.disable(self.entry_phone_guardator,self.my_phone_guardator)
        self.disable(self.entry_name_guardator,self.my_name_guardator)
        self.disable(self.entry_address_guardator,self.my_address_guardator)
        
    def save_credit_data(self,event):
       fee=self.empty_field(self.my_dues.get())
       product=self.empty_field(self.my_product.get())
       amount=self.empty_field(self.my_amount.get())
       if fee==False or product==False or amount==False:
           messagebox.showerror("Error","Los campos cuotas, productos, monto financiado no pueden estar vacios")
       else: 
           advance =0 if self.empty_field(self.my_advance.get())==False else check_float(self.my_advance.get())
           fee =check_integer(fee)
           amount=check_float(amount)
           if advance==None or fee==None or amount==None:
               messagebox.showerror("Error","Los campos cuotas, anticipo, monto financiado no se completaron correctamente")
           else:
            if amount>advance:
                fee_amount=math.ceil((amount/fee)/10)*10
                on_auxiliary_account=advance-fee_amount
                pay=fee_amount
                on_account=advance
                if on_auxiliary_account<0:
                    on_account=advance
                    pay=fee_amount-advance   
                elif on_auxiliary_account==0:
                    on_account=0
                    fee=fee-1
                else:
                    fee=fee-1 
                while on_auxiliary_account>0:
                    on_auxiliary_account=on_auxiliary_account-fee_amount
                    if on_auxiliary_account<0:
                        on_account=on_auxiliary_account+fee_amount
                        pay=fee_amount-on_account
                    elif on_auxiliary_account==0:
                        on_account=0
                        fee=fee-1
                    else:
                        fee=fee-1 
                self.first_date=self.cal_1.get_date()
                self.second_date=self.cal_2.get_date()  
                self.third_date=self.cal_3.get_date()
                expiration_dates=self.generate_expiration_dates(self.first_date,self.second_date,fee,on_account)  
                phone_guardator=self.empty_field(self.my_phone_guardator.get())
                name_guardator=self.empty_field(self.my_name_guardator.get())
                adress_guardator=self.empty_field(self.my_address_guardator.get())    
                phone_guardator ="No fue cargado" if phone_guardator==False else phone_guardator
                adress_guardator ="No fue cargado" if adress_guardator==False else adress_guardator
                name_guardator ="No fue cargado" if name_guardator==False else name_guardator 
                new_credit=Credits(self.account,fee,product,amount,datetime.datetime.strftime(self.third_date,"%Y%m%d"))
                fee=int(self.my_dues.get())
                third_date_str=datetime.datetime.strftime(self.third_date,"%Y%m%d")
                mensaje=f"""Generación de nuevo credito a cliente con nombre {self.name}, cuyo dni es {self.dni} por los productos de {new_credit.products} por total de monto financiado de {new_credit.amount}, con un anticipo de {advance}, quedando a cuenta {on_account}, en {new_credit.fee} cuotas de {math.ceil((new_credit.amount/fee)/10)*10} con el primer vencimiento el día  {processes_data_date(expiration_dates[0][0])} debe pagar la suma de {pay} con garante {name_guardator} cuyo telefono es {phone_guardator} y su direccion es {adress_guardator} generado en la fecha {processes_data_date(third_date_str)}"""

                ask = messagebox.askyesno("Generación de nuevo credito", mensaje)
                if ask: 
                    write_new_credit(new_credit)
                    max_id_credit=search_maximum_credit()
                    write_expiration_dates(max_id_credit,expiration_dates,math.ceil((new_credit.amount/fee)/10)*10)
                    new_guardator=Guardator(name_guardator,adress_guardator,phone_guardator,max_id_credit)
                    write_new_guardator(new_guardator)
                    messagebox.showinfo("Generación de nuevo credito",f"Generación exito de credito, el número es {max_id_credit}")
                    self.disenable_change_field()
                    self.clean(self.entry_account,self.my_account)
                    self.my_account_name.set("")
                    self.my_account_dni.set("")
            else:
                   messagebox.showerror("Error","El anticipo es mayor o igual que el monto financiado")

    def generate_expiration_dates(self,first_date,second_date,fee,on_account):
        """_summary_

        Args:
            first_date (_type_): _description_
            second_date (_type_): _description_
            fee (_type_): _description_

        Returns:
            _type_: _description_
        """        
        delta_day=datetime.timedelta(days=30)
        list_expirate_days=[]
        if(first_date>=second_date):
              date_str=datetime.datetime.strftime(first_date,"%Y%m%d")
              list_expirate_days.append([date_str,on_account])
              date=first_date
              for i in range(fee-1): 
                   date=date+delta_day
                   date_str=datetime.datetime.strftime(date,"%Y%m%d")
                   list_expirate_days.append([date_str,0.0])   
              return list_expirate_days
        else:
              date_str=datetime.datetime.strftime(first_date,"%Y%m%d")
              list_expirate_days.append([date_str,on_account])
              
              date_str=datetime.datetime.strftime(second_date,"%Y%m%d")
              list_expirate_days.append([date_str,0.0])
              date=second_date
              for i in range(fee-2): 
                   date=date+delta_day
                   date_str=datetime.datetime.strftime(date,"%Y%m%d")
                   list_expirate_days.append([date_str,0.0])
              return list_expirate_days
              
    def qualification (self,info):
        info=processes_data_date(info)
        expiration_date = datetime.datetime.strptime(info,'%Y-%m-%d') 
        expiration_date=expiration_date.date()
        difference=expiration_date-self.today
        difference=int (difference.days)
        if difference>=0:
            return "Muy bien"
        elif difference>=-10 and difference<0:
            return "Muy Mal"
        else:
            return "pesimo"
       

               
           