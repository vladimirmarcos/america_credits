import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from  tkcalendar import DateEntry

from ..search.frame_search import FrameSearch

import processes
from processes.math_processes import check_integer,check_float
from processes.str_and_date_processes import process_data_str_to_date,processes_data_date

import models
from models.credit_dao import search_account_credits_info,search_all_credit_info,search_product,search_mora,interest_calculation, update_quote,writte_new_pay,search_rest_credit,delete_credit,generate_payment_receipt
from models.account_dao import search_data_account
from models.models import Pay

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
        self.label_account.grid(row=2,column=0,sticky="nsew")
        

        self.cal_1=DateEntry(self,
                           width=10,
                           locale='es_ES',
                           date_pattern='dd-mm-y')
        self.cal_1.grid(row=1,column=1,sticky="nsew")

        self.my_account=tk.StringVar()
        self.entry_account=tk.Entry(self,textvariable=self.my_account,justify="left")
        self.entry_account.config(font=('Arial',12),width=10)
        self.entry_account.grid(row=2,column=1,sticky="nsew")
        self.entry_account.bind ("<Return>",self.look_for_account)

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
        self.mora=search_mora()
        self.my_mora.set(str(self.mora)+" %")
        self.label_date=tk.Label(self,text='Fecha Pago',justify="left",anchor="w",font=('Arial',12,'bold'))
        self.label_date.grid(row=1,column=0,sticky="nsew")
       

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

        self.button_pay=tk.Button(self,text="Generar Pago",command=self.generate_pay)
        self.button_pay.config(width=len ("Generar Pago "),font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',activebackground='#35BD6F',state="disabled") 
        self.button_pay.grid (row=2,column=11)
                            
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
            self.entry_money_received[i].bind("<Return>",self.check_money)
            t+=1
        
    def look_for_account(self,event):
        self.check_account(check_integer(self.my_account.get()),self.load_info_account,self.my_account.get())

    def load_info_account(self):
        data=search_data_account(self.account)
        self.name=data[0]
        self.dni=data[1]
        self.address=data[3]
        ask= messagebox.askyesno("Consulta", f"El cliente asociado al número {self.account} es {self.name}, su D.N.I. es {self.dni} y su dirección es {self.address} ")
        if ask:
            self.info=search_account_credits_info(self.account)
            if self.info!=[]:
                self.date_pay=self.cal_1.get_date()
                self.button_pay.config(state="normal") 
                self.my_new_mora.set("")
                self.entry_new_mora.config(state='normal')
                self.entry_new_mora.focus()
                self.my_name.set(self.name)
                self.my_dni.set(self.dni)
                self.credits_list=self.generates_credit_dictionary(self.info)
                for item in self.credit.get_children():
                    self.credit.delete(item)
                j=0
                for i in self.info: 
                 product=search_product(i)
                 self.credit.insert('', j, iid=i, text=f'credito {i}: {product}')
                 j+=1
                self.credit.bind('<<TreeviewSelect>>', self.load_info_credit)
                self.credit.selection_set(self.credit.get_children()[0])
            else:
                messagebox.showerror("No se encontro creditos",f"La cuenta con número {self.account} no tiene asociada ningun credito")

    def load_info_credit(self,event):
        self.clean_data()
        self.current_credit=int (self.credit.selection()[0])
        self.current_data_credit=self.credits_list[self.current_credit]
        t=0
        for i in self.current_data_credit:
            self.load_date_info(i,t)
            t+=1

    def check_money(self,event):
        message=""
        message_succeful=f"Dinero recibido de credito {self.current_credit} para cuotas: \n"
        auxiliary=[]
        t=0
        for i in self.current_data_credit:

            money_aux=0 if self.money_received[t].get()=="" else check_float(self.money_received[t].get())
            if money_aux==None:
                message=message+f"\n el dato {self.money_received[t].get()} de la cuota {t+1} del credito {self.current_credit} no es un dato valido como dinero recibido"
            else:
                if money_aux!=0:
                    message_succeful=message_succeful+f"monto {money_aux} para cuota {str(t+1)} \n"
                auxiliary.append(money_aux)
            t+=1
        if message!="":
            messagebox.showerror("Info",message)
            return 
        else:
            list_pay_credit=self.credits_list[self.current_credit]
            t=0
            for i in auxiliary:
                list_pay_credit[t][6]=i
                t+=1
            self.credits_list[self.current_credit]=list_pay_credit
            messagebox.showinfo("Datos ingresados",message_succeful)
            return 

    def clean_data(self):
        t=0
        for i in range(12):
            self.quote[i].set("")
            self.expirate_date[i].set("")
            self.amount[i].set("")
            self.interests[i].set("")
            self.on_account[i].set("")
            self.total[i].set("")
            self.missing[i].set("")
            self.money_received[i].set("")
            self.entry_money_received[i].config(state="disabled")
            t+=1

    def load_date_info(self,i,t):
            self.quote[t].set(i[2])
            self.expirate_date[t].set(processes_data_date(i[1]))
            self.amount[t].set(i[3])
            self.interests[t].set(self.calculate_interest(i))
            self.on_account[t].set(i[4])
            self.total[t].set(i[3]+self.calculate_interest(i))
            self.missing[t].set(i[3]+self.calculate_interest(i)-i[4])
            if i[6]=="":
                self.money_received[t].set(0)
            else:
                self.money_received[t].set(i[6])
            self.entry_money_received[t].config(state="normal")
            
    def calculate_interest(self,list_information):
        date=process_data_str_to_date(list_information[1])
        date=date.date()
        if date > self.date_pay:
            interest=0
            return interest   
        else:
            interest=interest_calculation(self.date_pay,date,list_information[3],self.mora)
            return interest
            
    def generate_pay(self):
        self.new_moratoria=" " if self.my_new_mora.get()=="" else check_float(self.my_new_mora.get())
        dictionary_pay={}
        flag_pay=0
        if self.new_moratoria or self.new_moratoria==0:
            if self.new_moratoria!=" ":
                self.moratoria_calculo=self.new_moratoria
            else:
                self.moratoria_calculo=self.mora
            keys = list(self.credits_list.keys())
            messege_pay="Se ejecutara el pago por \n"
            messege_error="Error al ejecutar el pago de  \n"
            list_dates=""
            for i in keys:
                list_dates=self.credits_list[i]
                messege_pay=messege_pay+f"Credito número {i}\n"
                flag=0
                t=0 
                auxiliary_messege_error=""
                for j in list_dates:
                    if j[6]!=0.0:
                        flag_pay=1
                        expirate_date=process_data_str_to_date(j[1])
                        expirate_date=expirate_date.date()
                        if expirate_date > self.date_pay:
                            interest=0
                            total=j[3]
                        else:
                            interest=interest_calculation(self.date_pay,expirate_date,j[3],self.moratoria_calculo)
                            total=j[3]+interest
                        rest=total-(j[4]+j[6])
                        if rest>0:
                            messege_pay=messege_pay+f"dinero a cuenta para cuota {j[2]} por un valor de {j[6]}\n"
                            list_dates[t][7]="A cuenta"
                        elif rest==0.0:
                            messege_pay=messege_pay+f"pago cuota {j[2]} por un valor de {j[6]} recibido para finalizar\n"
                            list_dates[t][7]="Cuota Cancelada"
                        else:
                            auxiliary_messege_error=auxiliary_messege_error+f"el valor total de la cuota {j[2]} es de {total} recuerde que tiene a cuenta {j[4]} y la mora es de {self.moratoria_calculo} verifique el monto ingresado o modifique la mora"  
                            flag=1
                            
                    t+=1
                if flag==1:
                    messege_error=messege_error+f"Credito número {i}\n"+ auxiliary_messege_error    
                    flag=0  
                self.credits_list[i]=list_dates
                

            if messege_error!= "Error al ejecutar el pago de  \n":
                messagebox.showerror("Error Pago", messege_error)
            else:
                if flag_pay==0:
                    messagebox.showerror("Error","No se ha ingresado ningún valor de dinero recibido en ningún crédito")
                else:
                    ask= messagebox.askyesno("Consulta", messege_pay+ "\n¿Esta seguro?")
                    if ask:
                     keys = list(self.credits_list.keys())
                     for i in keys:
                        list_dates=self.credits_list[i]
                        auxiiliary_list=[]
                        flag=0
                        for j in list_dates:
                            if j[7]!="":
                                if j[7]=="A cuenta":
                                  update_quote(j[6],j[5],i,j[2])
                                  j[5]=0
                                  j[7]=0
                                  del j[1]
                                  auxiiliary_list.append(j)
                                  
                                elif j[7]=="Cuota Cancelada":
                                 update_quote(j[6],j[7],i,j[2])
                                 j[5]=0
                                 j[7]=1
                                 del j[1]
                                 auxiiliary_list.append(j)
                                else:
                                    pass
                        if auxiiliary_list!=[]:
                            dictionary_pay[i]=auxiiliary_list
                        res_credit=search_rest_credit(i)
                        if res_credit:
                            pass
                        else:
                            delete_credit(i)
                            messagebox.showinfo("Finalizo crédito",f"Finalizo el credito número {i}")
                     new_pay=Pay(datetime.datetime.strftime(self.date_pay,"%Y%m%d"),dictionary_pay,self.account)
                     writte_new_pay(new_pay)
                     ask=messagebox.askyesno("Imprimir resumen","¿Desea imprimir el pago?")    
                     if ask:
                        generate_payment_receipt(datetime.datetime.strftime(self.date_pay,"%Y%m%d"),dictionary_pay,self.dni,self.name,self.account,1)
                        self.clean_data()
                        self.credit.bind('<<TreeviewSelect>>', "")
                        for item in self.credit.get_children():
                            self.credit.delete(item)
                        self.my_account.set("")
                        self.entry_account.focus()
                     else:
                        generate_payment_receipt(datetime.datetime.strftime(self.date_pay,"%Y%m%d"),dictionary_pay,self.dni,self.name,self.account,0)
                        self.clean_data()
                        self.credit.bind('<<TreeviewSelect>>', "")
                        for item in self.credit.get_children():
                            self.credit.delete(item)
                        self.my_account.set("")
                        self.entry_account.focus()
                                              
        else:
            messagebox.showerror("error al ingresar dato",f"el valor de dato {self.my_new_mora.get()} no es valido")    
            self.entry_new_mora.focus()

    def generates_credit_dictionary(self,list_credits):
        """_summary_

        Args:
            list_credits (_type_): _description_

        Returns:
            _type_: _description_
        """        
        my_credit_diccionary = {}
        for i in list_credits:  
            credit_list_info=[]
            rest_all_credits=search_all_credit_info(i)
            for j in rest_all_credits:
                auxiliar_list=[]
                auxiliar_list=j
                auxiliar_list.append(0.0)
                auxiliar_list.append("")
                credit_list_info.append(auxiliar_list)
            my_credit_diccionary[i]=credit_list_info  
        return my_credit_diccionary