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
        return f'Cuenta[{self.account_number},{self.name},{self.dni},{self.phone},{self.adress},{self.work_adress},{self.job}]'