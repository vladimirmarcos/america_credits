import tkinter as tk
from tkinter import messagebox

from ..search.frame_search import FrameSearch
import processes
from processes.math_processes import check_integer
from processes.str_and_date_processes import processes_data_str
import models
from models.account_dao import search_data_account,search_dni_account,update_data

class FrameChangeData(FrameSearch):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.serch_field()
        self.change_field()
    
    def change_field(self):
        self.label_account_number=tk.Label(self,text='Numero\ncuenta')
        self.label_account_number.config(font=('Arial',12,'bold'))
        self.label_account_number.grid(row=1,column=0)

        self.label_name=tk.Label(self,text='Nombre')
        self.label_name.config(font=('Arial',12,'bold'))
        self.label_name.grid(row=2,column=0)

        self.label_dni=tk.Label(self,text='D.N.I.')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=2,column=2)

        self.label_name_change=tk.Label(self,text='Nombre\n nuevo')
        self.label_name_change.config(font=('Arial',12,'bold'))
        self.label_name_change.grid(row=3,column=0)

        self.label_new_dni=tk.Label(self,text='D.N.I. \nnuevo')
        self.label_new_dni.config(font=('Arial',12,'bold'))
        self.label_new_dni.grid(row=3,column=2)

        self.label_new_adress=tk.Label(self,text='Domicilio \nNuevo')
        self.label_new_adress.config(font=('Arial',12,'bold'))
        self.label_new_adress.grid(row=3,column=4)
        
        self.label_new_phone=tk.Label(self,text='Telefono \nNuevo')
        self.label_new_phone.config(font=('Arial',12,'bold'))
        self.label_new_phone.grid(row=3,column=6)

        #Entrys de cada Campo

        self.my_account_number=tk.StringVar()
        self.entry_account_number=tk.Entry(self,textvariable=self.my_account_number)
        self.entry_account_number.config(width=15,font=('Arial',12))
        self.entry_account_number.grid(row=1,column=1)

        self.my_account_name=tk.StringVar()
        self.entry_account_name=tk.Entry(self,textvariable=self.my_account_name)
        self.entry_account_name.config(width=15,font=('Arial',12),state='disabled')
        self.entry_account_name.grid(row=2,column=1)
        

        self.my_account_dni=tk.StringVar()
        self.entry_account_dni=tk.Entry(self,textvariable=self.my_account_dni)
        self.entry_account_dni.config(width=15,font=('Arial',12),state='disabled')
        self.entry_account_dni.grid(row=2,column=3)

        self.my_new_name=tk.StringVar()
        self.entry_new_name=tk.Entry(self,textvariable=self.my_new_name)
        self.entry_new_name.config(width=15,font=('Arial',12),state='disabled')
        self.entry_new_name.grid(row=3,column=1)

        self.my_new_dni=tk.StringVar()
        self.entry_new_dni=tk.Entry(self,textvariable=self.my_new_dni)
        self.entry_new_dni.config(width=15,font=('Arial',12),state='disabled')
        self.entry_new_dni.grid(row=3,column=3)

        self.my_new_address=tk.StringVar()
        self.entry_new_address=tk.Entry(self,textvariable=self.my_new_address)
        self.entry_new_address.config(width=15,font=('Arial',12),state='disabled')
        self.entry_new_address.grid(row=3,column=5)

        self.my_new_phone=tk.StringVar()
        self.entry_new_phone=tk.Entry(self,textvariable=self.my_new_phone)
        self.entry_new_phone.config(width=15,font=('Arial',12),state='disabled')
        self.entry_new_phone.grid(row=3,column=7)

        #bind
        self.entry_account_number.bind ("<Return>",self.search_account)

    def search_account(self,event):
        account=check_integer(self.my_account_number.get())
        self.check_account(account,self.verify_account_data,self.my_account_number.get())
        
    def verify_account_data(self):
        data=search_data_account(self.account)
        self.name=data[0]
        self.dni=data[1]
        self.phone=data[2]
        self.address=data[3]
        ask= messagebox.askyesno("Consulta", f"El cliente asociado al número {self.account} es {self.name}, su D.N.I. es {self.dni} y su dirección es {self.address}")
        if ask:
             self.enable_change_fields()
    
    def enable_change_fields(self):
        """_summary_: Enable change fields
        """        
        self.my_account_name.set(self.name)
        self.my_account_dni.set(self.dni)

        self.entry_new_name.config(state="normal")
        self.entry_new_dni.config(state="normal")
        self.entry_new_address.config(state="normal")
        self.entry_new_phone.config(state="normal")
        self.entry_new_name.focus()

        self.entry_new_name.bind ("<Return>",self.change_data)
        self.entry_new_dni.bind ("<Return>",self.change_data)
        self.entry_new_address.bind ("<Return>",self.change_data)
        self.entry_new_phone.bind ("<Return>",self.change_data)
    
    def change_data(self,event):
        """_summary_: Change account information

        Args:
            event (_type_): _description_
        """        
        new_name=self.empty_field(self.my_new_name.get())
        new_dni=self.empty_field(self.my_new_dni.get())
        new_phone=self.empty_field(self.my_new_phone.get())
        new_address=self.empty_field(self.my_new_address.get())
        message=f"¿Esta seguro de cambiar de la cuenta {self.account} los siguientes datos\n "
        error_message=""
        change_list=[]
        if new_name==new_dni==new_phone==new_address==False:
            messagebox.showerror("Error","Se enviaron todos los campos vacíos" )
        else:
             if new_dni:
                 new_dni_check=check_integer(new_dni)
                 if new_dni_check:
                     new_dni_check=search_dni_account(new_dni_check)
                     if new_dni_check==None:
                        message=message+ f"el D.N.I. {self.dni} por {new_dni} \n"
                        change_list.append(["dni",new_dni])
                     else:
                         error_message=f"El dato {new_dni} ya esta asociado a la cuenta {new_dni_check}"
                 if new_dni_check==False:
                     error_message=f"El dato {new_dni} no es valido como D.N.I"
             if new_name:
                  message=message+ f"el Nombre {self.name} por {new_name} \n"
                  change_list.append(["nombre",new_name])
             if new_phone:
                 message=message+ f"el teléfono {self.phone} por {new_phone} \n"
                 change_list.append(["contacto_telefono",new_phone])
             if new_address:
                 message=message+ f"la direccion {self.address} por {new_address} \n"
                 change_list.append(["contacto_direccion",new_address])
             
             if error_message=="":
                 ask= messagebox.askyesno("Consulta", message)
                 if ask:
                    for i in change_list:
                        update_data(self.account,i[0],i[1])
                    messagebox.showinfo("Cambio exitoso","Se logro cambiar la información exitosamente")
                    self.disable_change_field()
             else:
                 messagebox.showerror("Error",error_message)
                       
    def disable_change_field(self):
        """_summary_: Disable change fields
        """        
        self.disable(self.entry_new_name,self.my_new_name)
        self.disable(self.entry_new_dni,self.my_new_dni)
        self.disable(self.entry_new_phone,self.my_new_phone)
        self.disable(self.entry_new_address,self.my_new_address)
        self.my_account_name.set("")
        self.my_account_dni.set("")
        self.my_account_number.set("")
        self.entry_account_number.focus()
        