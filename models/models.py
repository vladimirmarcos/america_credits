class Account:
     def __init__(self,account_number,name,dni,phone,adress,work_adress,job):
        self.account_id=None
        self.account_number=account_number
        self.name=name
        self.dni=dni
        self.phone=phone
        self.adress=adress
        self.work_adress=work_adress
        self.job=job 
        
     def __str__(self):
        return f'Account[{self.account_number},{self.name},{self.dni},{self.phone},{self.adress},{self.work_adress},{self.job}]'
     
class Credits:
    def __init__(self,account,fee,products,amount,issue_data):
        self.credito=None
        self.account=account
        self.fee=fee
        self.products=products
        self.amount=amount
        self.issue_data=issue_data
        self.state=1
            
    def __str__(self):
        return f'Credit[{self.account},{self.fee},{self.products},{self.amount},{self.issue_data},{self.state}]'
    

class Expiration_Dates:
    def __init__(self,date,amount,on_account,state,credit,fee):
        self.id_fecha=None
        self.date=date
        self.amount=amount  
        self.on_account=on_account      
        self.state=state
        self.credit=credit
        self.fee=fee
        
    def __str__(self):
        return f'Expiration Date[{self.date},{self.amount},{self.on_account},{self.state},{self.credit},{self.fee}]'

class Guardator:
    def __init__(self,name,address,phone,credit):
        self.id_guardator=None
        self.name=name
        self.address=address
        self.phone=phone
        self.credit=credit

    def __str__(self):
        return f'Guardator[{self.name},{self.address},{self.phone},{self.credit}]'
    
class Judicial:
    def __init__(self,account,amount,date):
        self.id_ju=None
        self.account=account
        self.amount=amount
        self.date=date
        self.state=1
        
    def __str__(self):
        return f'Judicial[{self.account},{self.amount},{self.date},{self.state}]'
    
class Judicial_info:
    def __init__(self,name,address,phone,product,judicial_credit):
        self.id_ju=None
        self.name=name
        self.address=address
        self.phone=phone
        self.product=product
        self.judicial_credit=judicial_credit
        
    def __str__(self):
        return f'Judicial_info[{self.name},{self.address},{self.phone},{self.product},{self.judicial_credit}]'

class Pay:
    def __init__(self,date,data,account):
        self.id_pagos=None
        self.date=date
        self.data=data 
        self.account=account
    def __str__(self):
        return f'Pay[{self.date},{self.data},{self.account}]'