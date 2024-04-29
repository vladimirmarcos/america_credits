import tkinter as tk

from windows.account.frame_new_account import FrameNewAccount
from windows.account.frame_change_account_data import FrameChangeData
from windows.credits.frame_new_credit import FrameNewCredit
from windows.credits.frame_delete_credit import FrameDeleteCredit

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