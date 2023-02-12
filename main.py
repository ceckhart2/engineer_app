import tkinter as tk
from mohr_page import MohrStuff


class MasterTk:
    def __init__(self, master):
        self.master = master
        self.master.title("Home Page")

        self.master.geometry('200x200')

        title = tk.Label(self.master, text='Main Menu', font=('Arial', 25))

        mohr_button = tk.Button(self.master, text="Mohr's Circle", command=self.open_mohr)

        title.pack()
        mohr_button.pack(pady=10)

        self.master.mainloop()

    def open_mohr(self):
        mohr_page = MohrStuff()

if __name__ == '__main__':
    root = tk.Tk()
    m1 = MasterTk(root)

