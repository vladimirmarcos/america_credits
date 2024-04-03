import tkinter as tk
from tkinter import messagebox
import sqlite3

import models
from models.account_dao import search_name_account


class FrameSearch(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def serch_field(self):
        """_summary_:Position the name search label and entry search name
        """       
        self.label_search_name=tk.Label(self,text='Busqueda\n nombre',justify="left")
        self.label_search_name.config(font=('Arial',12,'bold'))
        self.label_search_name.grid(row=0,column=0)

        self.search_mi_name=tk.StringVar()
        self.entry_search_name=tk.Entry(self,textvariable=self.search_mi_name)
        self.entry_search_name.config(width=20,font=('Arial',12))
        self.entry_search_name.grid(row=0,column=1,sticky="w")
        self.entry_search_name.bind ("<Return>",self.search_name)

        self._frame = None

    def search_name(self,event):
         """_summary_:searches for the name, if similarities are found, it returns a list with all of them, otherwise it warns that it was not found.Also, let us know if there is a problem accessing the database.

        Args:
            event (enter): The expected event is for the user to press the enter key.
        """         
         name=self.search_mi_name.get()
         if name !="":
                        list_name=search_name_account ("nombre",name)
                        if list_name:
                                list_account=[list(x) for x in list_name]
                                title=f" Usuarios con nombre {name}"
                                message= "\n"
                                for i in list_account:
                                         message=message+ str(i[2])+ " dni "+ str(i[0])+" domicilio "+ str(i[3])+ " N cuenta "+str(i[1])+" \n"
                                messagebox.showinfo(title,message)  
                                self.clean(self.entry_search_name,self.search_mi_name) 
                        else: 
                                messagebox.showerror("No se encontro nombre",f"el nombre {name} no tiene asociada ninguna cuenta" )                     
         else:
              messagebox.showerror("No ingreso nombre","Se envio el campo vacío" )

    def clean(self,field,values):
          """_summary_:clears the specified field

        Args:
            field (Entry):_description_
            values (StringVar): _description_
        """          
          values.set("")
          field.focus()

    def disable(self,field,values):
           """_summary_:disables the specified field

        Args:
            field (Entry): _description_
            values (StringVar): _description_
        """         
           values.set("")
           field.config(state='disabled')

    def empty_field(self,field):
          """_summary_: check empty field

        Args:
            field (Entry): _description_

        Returns:
            False: In case of empty field
            Field: In case of non-empty field
        """          
          if field=="":
                return False
          else:
                return field

    def field_function(self,field,key,funcion):
          """_summary_:assign function to entry field

        Args:
            field (Entry): _description_
            key (keyboard key): _description_
            funcion (function to execute): _description_
        """         
          field.bind(key,funcion)
    

    def delete(self):
        self.pack_forget()
        self.destroy()