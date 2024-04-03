import tkinter as tk
from tkinter import messagebox

from ..search.frame_search import FrameSearch
import processes
from processes.math_processes import check_integer
import models
from models.account_dao import search_dni_account,max_account,save_new_account
from models.models import Account


class FrameNewAccount(FrameSearch):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.field_new_account()
        
    def field_new_account(self):

        #label de campos
        self.label_name=tk.Label(self,text='Nombre ',justify="left")
        self.label_name.config(font=('Arial',12,'bold'))
        self.label_name.grid(row=1,column=0,pady=10,sticky="w")

        self.label_dni=tk.Label(self,text='DNI ',justify="right")
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=1,column=2,pady=10)

        self.label_phone=tk.Label(self,text='Teléfono',justify="left")
        self.label_phone.config(font=('Arial',12,'bold'))
        self.label_phone.grid(row=1,column=4,pady=10,sticky="w")

        self.label_address=tk.Label(self,text='Domicilio',justify="left")
        self.label_address.config(font=('Arial',12,'bold'))
        self.label_address.grid(row=1,column=6,pady=10,sticky="w")


        self.label_work_address=tk.Label(self,text='Domicilio \nTrabajo',justify="left")
        self.label_work_address.config(font=('Arial',12,'bold'))
        self.label_work_address.grid(row=2,column=0,pady=10,sticky="w")

        self.label_job=tk.Label(self,text='Puesto',justify="left")
        self.label_job.config(font=('Arial',12,'bold'))
        self.label_job.grid(row=2,column=2,pady=10,sticky="w")

        #Entrys de cada Campo
        self.entry_list=[]

        self.my_name=tk.StringVar()
        self.entry_name=tk.Entry(self,textvariable=self.my_name)
        self.entry_name.config(width=20,font=('Arial',12))
        self.entry_name.grid(row=1,column=1,pady=10,sticky="w")
        self.entry_list.append(self.entry_name)
        

        self.my_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.my_dni)
        self.entry_dni.config(width=15,font=('Arial',12))
        self.entry_dni.grid(row=1,column=3,pady=10,sticky="w")
        self.entry_list.append(self.entry_dni)
        

        self.my_phone=tk.StringVar()
        self.entry_phone=tk.Entry(self,textvariable=self.my_phone)
        self.entry_phone.config(width=15,font=('Arial',12))
        self.entry_phone.grid(row=1,column=5,pady=10,sticky="w")
        self.entry_list.append(self.entry_phone)
        

        self.my_address=tk.StringVar()
        self.entry_adress=tk.Entry(self,textvariable=self.my_address)
        self.entry_adress.config(width=20,font=('Arial',12))
        self.entry_adress.grid(row=1,column=7,pady=10,sticky="w")
        self.entry_list.append(self.entry_adress)
        

        self.my_work_address=tk.StringVar()
        self.entry_work_address=tk.Entry(self,textvariable=self.my_work_address)
        self.entry_work_address.config(width=20,font=('Arial',12))
        self.entry_work_address.grid(row=2,column=1,pady=10,sticky="w")
        self.entry_list.append(self.entry_work_address)
        

        self.my_job=tk.StringVar()
        self.entry_job=tk.Entry(self,textvariable=self.my_job)
        self.entry_job.config(width=15,font=('Arial',12))
        self.entry_job.grid(row=2,column=3,pady=10,sticky="w")
        self.entry_list.append(self.entry_job)

        self.entry_name.focus()
    
        self._frame = None

        [self.field_function(x,"<Return>",self.save_data) for x in self.entry_list]
    
    def save_data(self,event):
        """_summary_: Save account data

        Args:
            event (_type_): _description_
        """        
        name=self.empty_field( self.my_name.get())
        dni=self.empty_field( self.my_dni.get())
        phone=self.empty_field( self.my_phone.get())
        adress=self.empty_field( self.my_address.get())
        work_adress=self.empty_field( self.my_work_address.get())
        job=self.empty_field( self.my_job.get())

        if name and dni:
            dni=check_integer(dni)
            if dni:
                dni_check=search_dni_account(dni)
                if dni_check==None:
                            phone ="No fue cargado" if phone==False else phone
                            adress ="No fue cargado" if adress==False else adress
                            work_adress ="No fue cargado" if work_adress==False else work_adress
                            job ="No fue cargado" if job==False else job
        
                            New_account=Account(max_account(),
                                                name,
                                                dni,
                                                adress,
                                                phone,
                                                work_adress,
                                                job)
                            title="Generación de nueva cuenta"
                            message=f"Generación de nueva cuenta de cliente con nombre {New_account.name}, con dni {New_account.dni}, con domicilio en {New_account.adress}, con telefono {New_account.phone}, con domicilio de trabajo es {New_account.work_adress} cuya función es {New_account.job}"
                            
                            ask = messagebox.askyesno(title, message)
                            if ask:
                                  save_new_account(New_account)
                                  messagebox.showinfo("Carga existosa de nueva cuenta",f"La cuenta para el cliente {name} fue creada exitosamente, su número es {New_account.account_number}")
                                  self.clean_new_account_field()
                else:       
                            messagebox.showerror("Error por dato ya existent",f"el dni {dni} ya esta registrado con la cuenta {dni_check}")
                            
            else:
                messagebox.showerror("Error al ingresar dato",f"el dato {self.my_dni.get()} no es valido como D.N.I.")
                
                
                
        else:
              messagebox.showerror("Error por campos vacios","El campo nombre o D.N.I. o ambos se encuentran vacíos, se necesita de ambos campos para crear la cuenta")
             
    def clean_new_account_field(self):
          self.clean(self.entry_name,self.my_name)
          self.clean(self.entry_dni,self.my_dni)
          self.clean(self.entry_phone,self.my_phone)
          self.clean(self.entry_adress,self.my_address)
          self.clean(self.entry_work_address,self.my_work_address)
          self.clean(self.entry_job,self.my_job)
          self.entry_name.focus()