import tkinter as tk
from tkinter import messagebox
from  tkcalendar import DateEntry
import datetime

import models
from models.reports_dao import create_reports_credits,create_reports_credits_excel

from .frame_reports import FrameReports
class FrameReportsCredits(FrameReports):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.reports_field()
    def generate_reports(self):

        date_1=self.cal_1.get_date()
        date_2=self.cal_2.get_date()
        if date_1<=date_2:
            fecha_texto_1=datetime.datetime.strftime(date_1,"%Y%m%d")
            fecha_texto_2=datetime.datetime.strftime(date_2,"%Y%m%d")
            create_reports_credits(fecha_texto_1,fecha_texto_2)
        else:
            messagebox.showerror("Error al generar informe","La fecha de inicio debe ser menor o igual a la fecha cierre")
    def generate_reports_excel(self):
        date_1=self.cal_1.get_date()
        date_2=self.cal_2.get_date()
        if date_1<=date_2:
            fecha_texto_1=datetime.datetime.strftime(date_1,"%Y%m%d")
            fecha_texto_2=datetime.datetime.strftime(date_2,"%Y%m%d")
            create_reports_credits_excel(fecha_texto_1,fecha_texto_2)
        else:
            messagebox.showerror("Error al generar informe","La fecha de inicio debe ser menor o igual a la fecha cierre")