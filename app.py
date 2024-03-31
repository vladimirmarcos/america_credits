import tkinter as tk
from menu.menu import App


def main():
    ventana = tk.Tk()
    ventana.geometry("1200x1200")
    App(ventana).pack(side="top", fill="both", expand=True)
    ventana.mainloop()


if __name__=='__main__':
    
    main()