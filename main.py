import tkinter as tk
from mohr_page import MohrStuff
from tkinter import messagebox
from unit_conversions import ConversionPage

class MasterTk:
    # Initialize page details
    def __init__(self, master):
        self.master = master
        self.master.title("Home Page")

        # Page size
        self.master.geometry('200x200')

        # Closing Protocol
        self.master.protocol('WM_DELETE_WINDOW', self.on_closing)

        title = tk.Label(self.master, text='Main Menu', font=('Arial', 25))

        #Buttons for other pages
        mohr_button = tk.Button(self.master, text="Mohr's Circle", command=self.open_mohr)
        conversion_button = tk.Button(self.master, text="Unit Conversions", command=self.open_conversion)


        title.pack()
        mohr_button.pack(pady=10)
        conversion_button.pack()

        self.master.mainloop()

    def on_closing(self):
        if messagebox.askyesno(message='Are you sure you want to Quit?'):
            self.master.destroy()

    def open_mohr(self):
        mohr_page = MohrStuff()

    def open_conversion(self):
        c1 = ConversionPage()


if __name__ == '__main__':
    root = tk.Tk()
    m1 = MasterTk(root)
