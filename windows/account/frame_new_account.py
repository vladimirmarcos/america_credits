import tkinter as tk
from ..search.frame_search import FrameSearch


class FrameNewAccount(FrameSearch):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.serch_field()
        self.field_new_account()
        self.disable_field_account()


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
        

        self.my_name=tk.StringVar()
        self.entry_name=tk.Entry(self,textvariable=self.my_name)
        self.entry_name.config(width=20,font=('Arial',12))
        self.entry_name.grid(row=1,column=1,pady=10,sticky="w")
        

        self.my_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.my_dni)
        self.entry_dni.config(width=15,font=('Arial',12))
        self.entry_dni.grid(row=1,column=3,pady=10,sticky="w")
        

        self.my_phone=tk.StringVar()
        self.entry_phone=tk.Entry(self,textvariable=self.my_phone)
        self.entry_phone.config(width=15,font=('Arial',12))
        self.entry_phone.grid(row=1,column=5,pady=10,sticky="w")
        

        self.my_address=tk.StringVar()
        self.entry_adress=tk.Entry(self,textvariable=self.my_address)
        self.entry_adress.config(width=20,font=('Arial',12))
        self.entry_adress.grid(row=1,column=7,pady=10,sticky="w")
        

        self.my_work_address=tk.StringVar()
        self.entry_work_address=tk.Entry(self,textvariable=self.my_work_address)
        self.entry_work_address.config(width=20,font=('Arial',12))
        self.entry_work_address.grid(row=2,column=1,pady=10,sticky="w")
        

        self.my_job=tk.StringVar()
        self.entry_job=tk.Entry(self,textvariable=self.my_job)
        self.entry_job.config(width=15,font=('Arial',12))
        self.entry_job.grid(row=2,column=3,pady=10,sticky="w")
    
        self._frame = None
    
   