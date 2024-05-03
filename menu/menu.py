import tkinter as tk

from windows.account.frame_new_account import FrameNewAccount
from windows.account.frame_change_account_data import FrameChangeData
from windows.credits.frame_new_credit import FrameNewCredit
from windows.credits.frame_delete_credit import FrameDeleteCredit
from windows.credits.frame_judical_credit import FrameJudicialCredit
from windows.payments.frame_payments import FramePayments
from windows.reports.frame_report_credit import FrameReportsCredits
from windows.reports.frame_report_pay import FrameReportsPay
from windows.reports.freme_rest_credit import FrameReportsRestCredit
from windows.reports.frame_morosos_reports import FrameReportsMorosos

class App(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)

        self.menu_account= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Cuentas", menu=self.menu_account)
        self.menu_account.add_command(label="Crear Nueva Cuenta",command=self.create_new_account)
        self.menu_account.add_command(label="Modificar Datos Cuenta",command=self.change_data_account)
        
        self.menu_credit= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Creditos", menu=self.menu_credit)
        self.menu_credit.add_command(label="Crear Nuevo Credito",command=self.create_new_credit)
        self.menu_credit.add_command(label="Eliminar Credito",command=self.delete_credit)
        self.menu_credit.add_command(label="Enviar Credito a Judiciales",command=self.judicial_credit)

        self.menu_payments= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Pagos", menu=self.menu_payments)
        self.menu_payments.add_command(label="Pagos",command=self.payments)
        
        self.menu_reports= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Reporte", menu=self.menu_reports)
        self.menu_reports.add_command(label="Reporte créditos emitidos",command=self.reports_credits)
        self.menu_reports.add_command(label="Reporte recibimos emitidos",command=self.reports_pay)
        self.menu_reports.add_command(label="Reporte saldos totales",command=self.reports_rest_credit)
        self.menu_reports.add_command(label="Reporte Morosos",command=self.reports_morosos)

        parent.config(menu=self.menu)
        self._frame = None

    def create_new_account(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameNewAccount(self)

    def change_data_account(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameChangeData(self)

    def create_new_credit(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameNewCredit(self)

    def delete_credit(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameDeleteCredit(self)
    
    def judicial_credit(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameJudicialCredit(self)

    def payments(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FramePayments(self)

    def reports_credits(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameReportsCredits(self)

    def reports_pay(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameReportsPay(self)
    def reports_rest_credit(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameReportsRestCredit(self)
    def reports_morosos(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameReportsMorosos(self)