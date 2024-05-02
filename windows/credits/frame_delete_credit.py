import tkinter as tk
from tkinter import messagebox

from .credits import FrameRemoveCredit

class FrameDeleteCredit(FrameRemoveCredit):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.serch_field()
        self.delete_field()

