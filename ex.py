import tkinter as tk
from modules import *
import customtkinter as ctk

def main():
    windows =  ctk.CTk()
    ctk.set_appearance_mode('dark')
    
    #windows = ttk()
    window_width = 1230#windows.winfo_width()
    window_height = 650#windows.winfo_height()
    screen_width = windows.winfo_screenwidth()
    screen_height = windows.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    windows.geometry(f"{window_width}x{window_height}+{x}+{y}")
    #windows.geometry("x")
    windows.resizable(False,False)
    windows.title("File Explore")
    
    
    windows.mainloop()
    #dirCD()



if __name__ == "__main__":
    main()


















