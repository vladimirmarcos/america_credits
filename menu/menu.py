import tkinter as tk

from windows.account.frame_new_account import FrameNewAccount
from windows.account.frame_change_account_data import FrameChangeData

class App(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)

        self.menu_account= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Cuentas", menu=self.menu_account)
        self.menu_account.add_command(label="Crear Nueva Cuenta",command=self.create_new_account)
        self.menu_account.add_command(label="Modificar Datos Cuenta",command=self.change_data_account)

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