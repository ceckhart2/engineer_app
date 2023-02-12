import tkinter as tk
import mohrs_circle as mc
from tkinter import messagebox


class MohrStuff:

    def __init__(self, root):
        self.root = root

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.root.geometry('580x720')

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.columnconfigure(0, weight=1)
        self.entry_frame.columnconfigure(1, weight=3)

        self.label_main = tk.Label(self.root, text="Mohr's Circle Stress Calculator", font='Arial, 25')
        self.label_sigmax = tk.Label(self.entry_frame, text='Sigma x: ', font=('Arial, 20'))
        self.label_sigmay = tk.Label(self.entry_frame, text='Sigma y: ', font=('Arial, 20'))
        self.label_tauxy = tk.Label(self.entry_frame, text='Tau xy', font=('Arial, 20'))

        self.entry_sigmax = tk.Entry(self.entry_frame, width=10)
        self.entry_sigmay = tk.Entry(self.entry_frame, width=10)
        self.entry_tauxy = tk.Entry(self.entry_frame, width=10)

        self.button_calculate = tk.Button(self.entry_frame, text='Calculate', command=self.display_plot)

        # Placing Labels on frame grid
        self.label_main.pack()
        self.label_sigmax.grid(row=0, column=0)
        self.label_sigmay.grid(row=1, column=0)
        self.label_tauxy.grid(row=2, column=0)

        # Placing Entry Boxes on frame grid
        self.entry_sigmax.grid(row=0, column=1, )
        self.entry_sigmay.grid(row=1, column=1)
        self.entry_tauxy.grid(row=2, column=1)

        self.button_calculate.grid(row=3, column=1)

        # Adding Canvas
        self.can1 = mc.FigureCanvasTkAgg()

        #Packing Entry and labels frame
        self.entry_frame.pack(padx=10, pady=10)
        self.root.mainloop()

    def display_plot(self):
        self.can1.get_tk_widget().destroy()

        try:
            sigmax = float(self.entry_sigmax.get())
            sigmay = float(self.entry_sigmay.get())
            tauxy = float(self.entry_tauxy.get())
            m1 = mc.MohrsCircle(sigmax, sigmay, tauxy, units='Kpa')

            canvas = mc.FigureCanvasTkAgg(m1.circle_plot(), master=self.root)
            self.can1 = canvas

            canvas.get_tk_widget().pack(side='right')
        except:
            tk.messagebox.showerror(title='TypeError', message="Please enter valid number values.")

    def on_closing(self):
        if messagebox.askyesno(message='Are you sure you want to Quit?'):
            self.root.destroy()

if __name__ == '__main__':
    page1 = tk.Toplevel()
    MohrStuff(page1)
