import tkinter as tk
from windows.account.frame_new_account import FrameNewAccount
class App(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)

        self.menu_account= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Cuentas", menu=self.menu_account)
        self.menu_account.add_command(label="Crear Nueva Cuenta",command=self.create_new_account)

        parent.config(menu=self.menu)
        self._frame = None

    def create_new_account(self):
            if self._frame is not None:
               self._frame.delete()
               self._frame = None
            if self._frame is None:
               self._frame = FrameNewAccount(self)