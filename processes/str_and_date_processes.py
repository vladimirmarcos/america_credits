import datetime


def processes_data_str(data):
            """_summary_: 

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """        
            data=data.lower()
            data=data.strip()    
            data=data.title() 
            return data 

def processes_data_date(data):
     """_summary_:

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """     
     processed_data=list(data)
     processed_data.insert(4,"-")
     processed_data.insert(7,"-")
     processed_data = ''.join(map(str, processed_data))
     processed_data=processed_data.split("-")
     processed_data=str(processed_data[2])+"-"+str(processed_data[1])+"-"+str(processed_data[0])
     return processed_data


def process_data_str_to_date(data):
        date=datetime.datetime.strptime(data,"%Y%m%d")
        return date

def convert_to_month(mes):
        if mes==1:
            return "Enero"
        if mes==2:
            return "Febrero"
        if mes==3:
            return "Marzo"
        if mes==4:
            return "Abril"
        if mes==5:
            return "Mayo"
        if mes==6:
            return "Junio"
        if mes==7:
            return "Julio"
        if mes==8:
            return "Agosto"
        if mes==9:
            return "Septiembre"
        if mes==10:
            return "Octubre"
        if mes==11:
            return "Noviembre"
        if mes==12:
            return "Diciembre" 
        
        

