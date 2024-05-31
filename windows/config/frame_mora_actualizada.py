import tkinter as tk
from tkinter import messagebox
import sqlite3
import processes
from processes.math_processes import check_integer,check_float

import models
from models.credit_dao import search_mora, update_mora
class FrameActualizarMora(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_actualizar_mora()
        
       
        
    def campos_actualizar_mora(self):
       #busqueda nombre 
        self.moratoria_base=search_mora()
        self.current_arrears=tk.StringVar()
        self.current_arrears.set(f"Valor actual de mora es {self.moratoria_base}")
        label_current_arrears=tk.Entry(self,text=self.current_arrears,justify="left")
        label_current_arrears.config(font=('Arial',12,'bold'),width=24,state="disabled")
        label_current_arrears.grid(row=0,column=0,sticky="ew")

        self.new_current=tk.StringVar()
        self.new_current.set(f"Nuevo valor de Mora")
        label_new_current=tk.Entry(self,text=self.new_current,justify="left")
        label_new_current.config(font=('Arial',12,'bold'),width=24,state="disabled")
        label_new_current.grid(row=1,column=0,sticky="ew")
       

        self.mi_actualizar_mora=tk.StringVar()
        self.entry_actualizar_mora=tk.Entry(self,textvariable=self.mi_actualizar_mora)
        self.entry_actualizar_mora.config(width=20,font=('Arial',12))
        self.entry_actualizar_mora.grid(row=1,column=2)
        self.entry_actualizar_mora.bind ("<Return>",self.verificar_mora)

        self._frame = None
        
    

   

    

    

       

    def verificar_mora(self,event):
         self.moratoria=check_float(self.mi_actualizar_mora.get())
         if self.moratoria:
              titulo="Cambio de valor de Mora"
              mensaje= f"""¿Esta seguro de cambiar el valor de mora a {self.moratoria}?"""
              respuesta = messagebox.askyesno(titulo, mensaje)
              if respuesta:
                   update_mora(self.moratoria)
                   self.mi_actualizar_mora.set("")
                   self.current_arrears.set(f"Valor actual de mora es {self.moratoria}")
                   self.entry_actualizar_mora.focus()
         else:
              titulo=" Error al generar el pago"
              mensaje="El dato ingresado como cuota es invalido"
              messagebox.showerror(titulo,mensaje)    


   
              
    def delete(self):
          self.pack_forget()
          self.destroy()