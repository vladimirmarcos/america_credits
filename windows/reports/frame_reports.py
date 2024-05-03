import tkinter as tk
from tkinter import messagebox
from  tkcalendar import DateEntry
import datetime

import models
from models.reports_dao import create_reports_credits,create_reports_credits_excel

class FrameReports(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.reports_field()

    def reports_field(self):
       #busqueda nombre 
        self.label_first_day=tk.Label(self,text='Fecha inicio',justify="right")
        self.label_first_day.config(font=('Arial',12,'bold'))
        self.label_first_day.grid(row=0,column=0,pady=10)

        self.label_second_day=tk.Label(self,text='Fecha Cierre',justify="right")
        self.label_second_day.config(font=('Arial',12,'bold'))
        self.label_second_day.grid(row=1,column=0,pady=10)

        self.cal_1=DateEntry(self,
                           width=10,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_1.grid(row=0,column=1,pady=10,sticky="w")

        self.cal_2=DateEntry(self,
                           width=10,
                           locale='es_ES',
                           date_pattern='y-mm-dd')
        self.cal_2.grid(row=1,column=1,pady=10,sticky="w")


        self.button_report=tk.Button(self,text="Crear Informe",command=self.generate_reports)
        self.button_report.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.button_report.grid(row=0,column=4,pady=10)

        self.button_report_csv=tk.Button(self,text="Crear Informe excel",command=self.generate_reports_excel)
        self.button_report_csv.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.button_report_csv.grid(row=0,column=5,padx=10)
        self._frame = None

  
    def delete(self):
        self.pack_forget()
        self.destroy()