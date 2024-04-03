from tkinter import messagebox


def error_messege(title,message):
    """_summary_:Gives the error message

    Args:
        title (String): _description_
        message (String): _description_
    """    
    messagebox.showerror(title,message)

def successful_message(title,message):
    """_summary_:Gives the succesful message

    Args:
        title (String): _description_
        message (String): _description_
    """    
    messagebox.showinfo(title,message)
