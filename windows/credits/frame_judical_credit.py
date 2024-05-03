import datetime
import tkinter as tk
from tkinter import messagebox
from  tkcalendar import DateEntry

from .credits import FrameRemoveCredit

import models
from models.credit_dao import delete_credit,write_new_judicial_credit,write_new_judicial_info, delete_guardator
from models.models import Judicial,Judicial_info

import processes
from processes.str_and_date_processes import processes_data_date

class FrameJudicialCredit(FrameRemoveCredit):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.serch_field()
        self.delete_field()
    
    def delete_field(self):
        super().delete_field()
        self.label_credit_id_delete.destroy()
        self.entry_credit_id_delete.destroy()

        self.label_date=tk.Label(self,text='Fecha',justify="right")
        self.label_date.config(font=('Arial',12,'bold'))
        self.label_date.grid(row=4,column=0)
        self.cal=DateEntry(self,
                           width=15,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal.grid(row=4,column=1,pady=10,sticky="w")

        
        self.label_credit_id_delete=tk.Label(self,text='Cred. Judicial',justify="right")
        self.label_credit_id_delete.config(font=('Arial',12,'bold'))
        self.label_credit_id_delete.grid(row=5,column=0)

        
        self.my_credit_id_delete=tk.StringVar()
        self.entry_credit_id_delete=tk.Entry(self,textvariable=self.my_credit_id_delete)
        self.entry_credit_id_delete.config(font=('Arial',12),width=15,state='disabled')
        self.entry_credit_id_delete.grid(row=5,column=1,sticky="w",padx=5)
        self.entry_credit_id_delete.bind("<Return>",self.delete_credit)

    def messege_delete(self,id_credit_delete,k):
        guardator=self.guardator_name[k].get()
        product=self.product[k].get()
        amount=self.remaning_amount[k].get()
        phone_guardator=self.guardator_phone[k].get()
        address_guardator=self.guardator_address[k].get()
        date_str=datetime.datetime.strftime(self.cal.get_date(),"%Y%m%d")
        ask= messagebox.askyesno("Consulta", f"¿Esta seguro de enviar a Judiciales  al credito {id_credit_delete} de {self.name} por el producto {product} con un faltante para pagar de {amount} con garante {guardator} con número de teléfono {phone_guardator}, direccion en {address_guardator} enviado a judiciales la fecha {processes_data_date(date_str)}")    
        if ask:
            new_judicial=Judicial(self.account,amount,date_str)
            max_id=write_new_judicial_credit(new_judicial)
            new_info=Judicial_info(guardator,address_guardator,phone_guardator,product,max_id)
            write_new_judicial_info(new_info)
            delete_credit(id_credit_delete)
            delete_guardator(id_credit_delete)
            messagebox.showinfo("Se Mando a Judiciales",f"El credito {id_credit_delete} fue enviado a Judiciales exitosamente")
            self.clean_data()
            self.my_credit_id_delete.set("")
            self.entry_credit_id_delete.config(state='disabled')
            self.my_account.set("")
            self.my_account_dni.set("")
            self.my_account_name.set("")
            self.entry_account.focus()