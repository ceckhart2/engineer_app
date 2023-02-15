import tkinter as tk
from mohr_page import MohrStuff
from tkinter import messagebox


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

        mohr_button = tk.Button(self.master, text="Mohr's Circle", command=self.open_mohr)

        title.pack()
        mohr_button.pack(pady=10)

        self.master.mainloop()

    def on_closing(self):
        if messagebox.askyesno(message='Are you sure you want to Quit?'):
            self.master.destroy()

    def open_mohr(self):
        mohr_page = MohrStuff()


if __name__ == '__main__':
    root = tk.Tk()
    m1 = MasterTk(root)
