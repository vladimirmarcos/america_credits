import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from  tkcalendar import DateEntry

from ..search.frame_search import FrameSearch

class FramePayments(FrameSearch):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.serch_field()
        self.payments_field()
    
    def serch_field(self):
        super().serch_field()
        self.entry_search_name.config(width=22)

    def payments_field(self):
        
        self.label_account=tk.Label(self,text='Cuenta',justify="left",anchor="w")
        self.label_account.config(font=('Arial',12,'bold'),justify="left")
        self.label_account.grid(row=1,column=0,sticky="nsew")
        
        self.my_account=tk.StringVar()
        self.entry_account=tk.Entry(self,textvariable=self.my_account,justify="left")
        self.entry_account.config(font=('Arial',12),width=10)
        self.entry_account.grid(row=1,column=1,sticky="nsew")
        self.entry_account.bind ("<Return>","self.verifica_cuenta")

        self.label_name=tk.Label(self,text='Nombre',justify="left",anchor="w")
        self.label_name.config(font=('Arial',12,'bold'),justify="left")
        self.label_name.grid(row=0,column=7,sticky="nsew")

        self.my_name=tk.StringVar()
        self.my_name.set("")
        self.entry_name=tk.Entry(self,textvariable=self.my_name,justify="left",width=len("Faltante a Pagar"),state='disabled',font=('Arial',12,'bold'))
        self.entry_name.grid(row=0,column=8,sticky="nsew")

        self.label_dni=tk.Label(self,text='D.N.I.',justify="left",anchor="w")
        self.label_dni.config(font=('Arial',12,'bold'),justify="left")
        self.label_dni.grid(row=1,column=7,sticky="nsew")
        
        self.my_dni=tk.StringVar()
        self.my_dni.set("")
        self.entry_dni=tk.Entry(self,textvariable=self.my_dni,justify="left",font=('Arial',12,'bold'),width=15,state='disabled')
        self.entry_dni.grid(row=1,column=8,sticky="nsew")


        self.label_mora=tk.Label(self,text='Mora Ac.',justify="left",anchor="w")
        self.label_mora.config(font=('Arial',12,'bold'),justify="left")
        self.label_mora.grid(row=2,column=7,sticky="nsew")
        
        self.my_mora=tk.StringVar()
        self.my_mora.set("")
        self.entry_mora=tk.Entry(self,textvariable=self.my_mora,justify="left",font=('Arial',12,'bold'),width=15,state='disabled')
        self.entry_mora.grid(row=2,column=8,sticky="nsew")

        self.label_date=tk.Label(self,text='Fecha Pago',justify="left",anchor="w",font=('Arial',12,'bold'))
        self.label_date.grid(row=2,column=0,sticky="nsew")
        self.cal_1=DateEntry(self,
                           width=10,
                           locale='es_ES',
                           date_pattern='dd-mm-y')
        self.cal_1.grid(row=2,column=1,sticky="nsew")

        self.label_credit=tk.Label(self,text='N. Credito',justify="left",anchor="w",font=('Arial',12,'bold'))
        self.label_credit.grid(row=3,column=0,sticky="nsew")
        self.credit=ttk.Treeview(self)
        self.credit.config(height=1)
        self.credit.grid(row=3,column=1)

        self.label_new_mora=tk.Label(self,text='Mora.',justify="left",anchor="w")
        self.label_new_mora.config(font=('Arial',12,'bold'),justify="left")
        self.label_new_mora.grid(row=4,column=0,sticky="nsew")
        
        self.my_new_mora=tk.StringVar()
        self.my_new_mora.set("")
        self.entry_new_mora=tk.Entry(self,textvariable=self.my_new_mora,justify="left",font=('Arial',12,'bold'),width=15,state='disabled')
        self.entry_new_mora.grid(row=4,column=1,sticky="nsew")
    
        #self.entry_nombre.focus()
        self.quote = [0] * 12
        self.expirate_date = [0] * 12
        self.amount=[0] * 12
        self.interests=[0] * 12
        self.on_account=[0] * 12
        self.total=[0] * 12
        self.missing=[0] * 12
        self.money_received=[0] * 12
        self.entry_money_received=[0] * 12

        t=8
        quote=tk.StringVar()
        quote.set(f"Cuota")
        label_quote=tk.Entry(self,text=quote,justify="left")
        label_quote.config(font=('Arial',12,'bold'),width=len(f"Cuota"),state="disabled")
        label_quote.grid(row=t,column=2,sticky="ew")
             
        expirate_date=tk.StringVar()
        expirate_date.set(f"Ven")
        expirate_date=tk.Entry(self,text=expirate_date)
        expirate_date.config(font=('Arial',12,'bold'),width=10,state="disabled")
        expirate_date.grid(row=t,column=3,sticky="ew")

        amount=tk.StringVar()
        amount.set(f"Monto")
        label_amount=tk.Entry(self,text=amount)
        label_amount.config(font=('Arial',12,'bold'),width=8,state="disabled")
        label_amount.grid(row=t,column=4)

        interests=tk.StringVar()
        interests.set(f"Int")
        label_interests=tk.Entry(self,text=interests,justify="left")
        label_interests.config(font=('Arial',12,'bold'),width=8,state="disabled")
        label_interests.grid(row=t,column=5)

        
        on_account=tk.StringVar()
        on_account.set(f"A cuenta")
        label_on_account=tk.Entry(self,text=on_account,justify="left")
        label_on_account.config(font=('Arial',12,'bold'),width=8,state="disabled")
        label_on_account.grid(row=t,column=6)

        
        total=tk.StringVar()
        total.set(f"total")
        label_total=tk.Entry(self,text=total,justify="left")
        label_total.config(font=('Arial',12,'bold'),width=8,state="disabled")
        label_total.grid(row=t,column=7)

        missing_money=tk.StringVar()
        missing_money.set(f"Dinero Faltante")
        missing_money=tk.Entry(self,text=missing_money,justify="left")
        missing_money.config(font=('Arial',12,'bold'),width=len("Faltante a Pagar"),state="disabled")
        missing_money.grid(row=t,column=8)

        money_received_label=tk.StringVar()
        money_received_label.set("Dinero recibido")
        label_money_received=tk.Entry(self,text=money_received_label,justify="left")
        label_money_received.config(font=('Arial',12,'bold'),width=len("Dinero recibido"),state="disabled")
        label_money_received.grid(row=t,column=9)

        
        t+=1
        for i in range(12):
            self.quote[i]=tk.StringVar()
            
            label_quote=tk.Entry(self,text=self.quote[i],justify="left")
            label_quote.config(font=('Arial',12,'bold'),width=len(f"Cuota"),state="disabled")
            label_quote.grid(row=t,column=2,sticky="ew")

            self.expirate_date[i]=tk.StringVar()
            expirate_date=tk.Entry(self,text=self.expirate_date[i],justify="left")
            expirate_date.config(font=('Arial',12,'bold'),width=10,state="disabled")
            expirate_date.grid(row=t,column=3)
            

            self.amount[i]=tk.StringVar()
            label_monto=tk.Entry(self,text=self.amount[i],justify="left")
            label_monto.config(font=('Arial',12,'bold'),width=8,state="disabled")
            label_monto.grid(row=t,column=4)

            self.interests[i]=tk.StringVar()
            label_interests=tk.Entry(self,text=self.interests[i],justify="left")
            label_interests.config(font=('Arial',12,'bold'),width=8,state="disabled")
            label_interests.grid(row=t,column=5)

            self.on_account[i]=tk.StringVar()
            label_on_account=tk.Entry(self,text=self.on_account[i],justify="left")
            label_on_account.config(font=('Arial',12,'bold'),width=8,state="disabled")
            label_on_account.grid(row=t,column=6)

            self.total[i]=tk.StringVar()
            label_total=tk.Entry(self,text=self.total[i],justify="left")
            label_total.config(font=('Arial',12,'bold'),width=8,state="disabled")
            label_total.grid(row=t,column=7)


            self.missing[i]=tk.StringVar()
            label_missing=tk.Entry(self,text=self.missing[i],justify="left")
            label_missing.config(font=('Arial',12,'bold'),width=len("Faltante a Pagar"),state="disabled")
            label_missing.grid(row=t,column=8)

            self.money_received[i]=tk.StringVar()
            self.entry_money_received[i]=tk.Entry(self,text=self.money_received[i],justify="left")
            self.entry_money_received[i].config(font=('Arial',12,'bold'),width=len("Dinero recibido"),state="disabled")
            self.entry_money_received[i].grid(row=t,column=9)
            self.entry_money_received[i].bind("<Return>","self.recibir_dinero")
            t+=1
        
        
       