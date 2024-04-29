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
        
        

