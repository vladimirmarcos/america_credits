import tkinter as tk
from tkinter import messagebox
import math
import datetime

import models
from models.account_dao import search_data_account
from models.credit_dao import search_all_credit_account,search_info_guardator,delete_credit,calculate_rest_of_the_credits

import processes
from processes.math_processes import check_integer

from ..search.frame_search import FrameSearch

class FrameRemoveCredit(FrameSearch):
    def __init__(self, parent):
        super().__init__(parent)
        

    def delete_field(self):
        self.label_account=tk.Label(self,text='Cuenta',justify="right")
        self.label_account.config(font=('Arial',12,'bold'))
        self.label_account.grid(row=1,column=0,pady=10)

        self.my_account=tk.StringVar()
        self.entry_account=tk.Entry(self,textvariable=self.my_account)
        self.entry_account.config(font=('Arial',12),width=15)
        self.entry_account.grid(row=1,column=1,pady=10,sticky="w")
        self.entry_account.bind ("<Return>",self.search_account)

        self.label_name_account=tk.Label(self,text='Nombre\n de cuenta',justify="right")
        self.label_name_account.config(font=('Arial',12,'bold'))
        self.label_name_account.grid(row=2,column=0)

        self.label_dni_account=tk.Label(self,text='Dni de\n cuenta',justify="right")
        self.label_dni_account.config(font=('Arial',12,'bold'))
        self.label_dni_account.grid(row=3,column=0)

        self.label_credit_id_delete=tk.Label(self,text='Cred. eliminar',justify="right")
        self.label_credit_id_delete.config(font=('Arial',12,'bold'))
        self.label_credit_id_delete.grid(row=4,column=0)

        self.my_account_name=tk.StringVar()
        self.entry_account_name=tk.Entry(self,textvariable=self.my_account_name)
        self.entry_account_name.config(font=('Arial',12),width=15,state='disabled')
        self.entry_account_name.grid(row=2,column=1,sticky="w",padx=5)

        self.my_account_dni=tk.StringVar()
        self.entry_account_dni=tk.Entry(self,textvariable=self.my_account_dni)
        self.entry_account_dni.config(font=('Arial',12),width=15,state='disabled')
        self.entry_account_dni.grid(row=3,column=1,sticky="w",padx=5)

        self.my_credit_id_delete=tk.StringVar()
        self.entry_credit_id_delete=tk.Entry(self,textvariable=self.my_credit_id_delete)
        self.entry_credit_id_delete.config(font=('Arial',12),width=15,state='disabled')
        self.entry_credit_id_delete.grid(row=4,column=1,sticky="w",padx=5)
        self.entry_credit_id_delete.bind("<Return>",self.delete_credit)

        self.credit_id= [0] * 12
        self.product= [0] * 12
        self.remaning_amount=[0] * 12
        self.guardator_name=[0] * 12
        self.guardator_phone=[0] * 12
        self.guardator_address=[0] * 12

        t=5
        credit_id=tk.StringVar()
        credit_id.set("Id Credito")
        label_credit_id=tk.Entry(self,text=credit_id,justify="left")
        label_credit_id.config(font=('Arial',12,'bold'),width=len("Id Credito"),state="disabled")
        label_credit_id.grid(row=t,column=3,sticky="ew")
        
        product=tk.StringVar()
        product.set("Producto")
        label_product=tk.Entry(self,text=product)
        label_product.config(font=('Arial',12,'bold'),width=len("Producto"),state="disabled")
        label_product.grid(row=t,column=4)
             
        remaining_amount=tk.StringVar()
        remaining_amount.set("Monto restante pagar")
        remaining_amount=tk.Entry(self,text=remaining_amount)
        remaining_amount.config(font=('Arial',12,'bold'),width=len("Monto restante Pagar"),state="disabled")
        remaining_amount.grid(row=t,column=5,sticky="ew")

        guardator_name=tk.StringVar()
        guardator_name.set("Nombre Garante")
        label_guardator_name=tk.Entry(self,text=guardator_name)
        label_guardator_name.config(font=('Arial',12,'bold'),width=len("Nombre Garante"),state="disabled")
        label_guardator_name.grid(row=t,column=6)
        
        guardator_phone=tk.StringVar()
        guardator_phone.set("Telef. Garante")
        label_guardator_phone=tk.Entry(self,text=guardator_phone)
        label_guardator_phone.config(font=('Arial',12,'bold'),width=len("Telef. Garante"),state="disabled")
        label_guardator_phone.grid(row=t,column=7)

        guardator_address=tk.StringVar()
        guardator_address.set("Direcc. Garante")
        label_guardator_address=tk.Entry(self,text=guardator_address)
        label_guardator_address.config(font=('Arial',12,'bold'),width=len("Direcc. Garante"),state="disabled")
        label_guardator_address.grid(row=t,column=8)
        t+=1
        for i in range(12):
            self.credit_id[i]=tk.StringVar()
            label_credit=tk.Entry(self,text=self.credit_id[i],justify="left")
            label_credit.config(font=('Arial',12,'bold'),width=len("Id Credito"),state="disabled")
            label_credit.grid(row=t,column=3,sticky="ew")

            self.product[i]=tk.StringVar()
            product=tk.Entry(self,text=self.product[i],justify="left")
            product.config(font=('Arial',12,'bold'),width=len("Producto"),state="disabled")
            product.grid(row=t,column=4)
    
            self.remaning_amount[i]=tk.StringVar()
            label_remaning_amount=tk.Entry(self,text=self.remaning_amount[i],justify="left")
            label_remaning_amount.config(font=('Arial',12,'bold'),width=len("Monto restante pagar"),state="disabled")
            label_remaning_amount.grid(row=t,column=5)

            self.guardator_name[i]=tk.StringVar()
            label_guardator_name=tk.Entry(self,text=self.guardator_name[i],justify="left")
            label_guardator_name.config(font=('Arial',12,'bold'),width=len("Nombre Garante"),state="disabled")
            label_guardator_name.grid(row=t,column=6)

            self.guardator_phone[i]=tk.StringVar()
            label_guardator_phone=tk.Entry(self,text=self.guardator_phone[i],justify="left")
            label_guardator_phone.config(font=('Arial',12,'bold'),width=len("Telef. Garante"),state="disabled")
            label_guardator_phone.grid(row=t,column=7)

            self.guardator_address[i]=tk.StringVar()
            label_guardator_address=tk.Entry(self,text=self.guardator_address[i],justify="left")
            label_guardator_address.config(font=('Arial',12,'bold'),width=len("Direcc. Garante"),state="disabled")
            label_guardator_address.grid(row=t,column=8)
            t+=1
        
    def verify_account_data(self):
        data=search_data_account(self.account)
        self.name=data[0]
        self.dni=data[1]
        self.address=data[3]
        ask= messagebox.askyesno("Consulta", f"El cliente asociado al número {self.account} es {self.name}, su D.N.I. es {self.dni} y su dirección es {self.address} ")
        if ask:
            self.load_data()
            

    def load_data(self):
        self.list_credit_info=[]
        self.list_credit_info=search_all_credit_account(self.account)
        if self.list_credit_info:
            self.entry_credit_id_delete.config(state="normal")
            self.entry_credit_id_delete.focus()
            self.my_account_name.set(self.name)
            self.my_account_dni.set(self.dni)
            list_guardator=search_info_guardator(self.list_credit_info)
            self.today = datetime.datetime.now()
            self.today=self.today.date()
            rest_credit_list=calculate_rest_of_the_credits(self.list_credit_info,self.today)
            self.clean_data()
            t=0
            k=0
            f=0
            for i,j,h in zip( self.list_credit_info,list_guardator,rest_credit_list):
                self.credit_id[t].set(i[0])
                self.product[t].set(i[1])
                self.guardator_name[k].set(j[0])
                self.guardator_phone[k].set(j[1])
                self.guardator_address[k].set(j[2])
                self.remaning_amount[f].set(h)
                t+=1
                k+=1
                f+=1
            
        else:
            messagebox.showerror("No se encontraron créditos",f"No se encontro creditos asociados a la cuenta número {self.account}")

    def delete_credit(self,event):
        id_credit_delete=check_integer(self.my_credit_id_delete.get())
        if id_credit_delete:
            flag=0
            k=0
            for i in self.list_credit_info:
                if i[0]==id_credit_delete:
                    flag=1
                    break
                k+=1
            if flag==1:
                self.messege_delete(id_credit_delete,k)
            else:
                messagebox.showerror("Error al ingresar el id de credito",f"El id {id_credit_delete} no esta asociado a ningún credito de la cuenta {self.account}")

        else:
            messagebox.showerror("error al ingresar el id",f"El dato {self.my_credit_id_delete.get()} no es valido como dato de id")

    def messege_delete(self,id_credit_delete,k):
        guardator=self.guardator_name[k].get()
        product=self.product[k].get()
        amount=self.remaning_amount[k].get()
        phone_guardator=self.guardator_phone[k].get()
        address_guardator=self.guardator_address[k].get()
        ask= messagebox.askyesno("Consulta", f"¿Esta seguro de eliminar el credito {id_credit_delete} de {self.name} por el producto {product} con un faltante para pagar de {amount} con garante {guardator} con número de teléfono {phone_guardator} y direccion en {address_guardator}")    
        if ask:
            delete_credit(id_credit_delete)
            messagebox.showinfo("Se Borro el credito",f"El credito {id_credit_delete} fue borrado exitosamente")
            self.clean_data()
            self.my_credit_id_delete.set("")
            self.entry_credit_id_delete.config(state='disabled')
            self.my_account.set("")
            self.entry_account.focus()

    def clean_data(self):
        for i in range (12):
              self.credit_id[i].set("")
              self.product[i].set("")
              self.guardator_name[i].set("")
              self.guardator_phone[i].set("")
              self.guardator_address[i].set("")
              self.remaning_amount[i].set("")