import tkinter as tk
from tkinter import messagebox
from  tkcalendar import DateEntry

from ..search.frame_search import FrameSearch
import processes
from processes.math_processes import check_integer,check_float
from processes.str_and_date_processes import processes_data_str
import models
from models.account_dao import search_data_account,search_dni_account,update_data

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

        self.cal_1=DateEntry(self,
                           width=15,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_1.grid(row=3,column=1,pady=10,sticky="w")

        self.cal_2=DateEntry(self,
                           width=15,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
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
        
    def search_account(self,event):
        account=check_integer(self.my_account.get())
        self.check_account(account,self.verify_account_data)

    def verify_account_data(self):
        data=search_data_account(self.account)
        self.name=data[0]
        self.dni=data[1]
        self.address=data[3]
        ask= messagebox.askyesno("Consulta", f"El cliente asociado al número {self.account} es {self.name}, su D.N.I. es {self.dni} y su dirección es {self.address}")
        if ask:
             self.enable_change_fields()
    
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

    def save_credit_data(self,event):
       
       dues=self.empty_field(self.my_dues.get())
       product=self.empty_field(self.my_product.get())
       amount=self.empty_field(self.my_amount.get())
       
       if dues==False or product==False or amount==False:
           messagebox.showerror("Error","Los campos cuotas, productos, monto financiado no pueden estar vacios")
    
       else: 
           advance =0 if self.empty_field(self.my_advance.get())==False else check_float(self.my_advance.get())
           dues =check_integer(dues)
           amount=check_float(amount)
           if advance==None or dues==None or amount==None:
               messagebox.showerror("Error","Los campos cuotas, anticipo, monto financiado no se completaron correctamente")
           else: 
               product=processes_data_str(product)
               phone_guardator ="No fue cargado" if self.empty_field(self.my_phone_guardator.get())==False else self.empty_field(self.my_phone_guardator.get())
               name_guardator ="No fue cargado" if self.empty_field(self.my_name_guardator.get())==False else self.empty_field(self.my_name_guardator.get())

               address_guardator ="No fue cargado" if self.empty_field(self.my_address_guardator.get())==False else self.empty_field(self.my_address_guardator.get())

               print (phone_guardator)
               print (name_guardator)
               print (address_guardator)

               
           