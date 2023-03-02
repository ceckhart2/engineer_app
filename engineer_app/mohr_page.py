import tkinter as tk
from engineer_app import mohrs_circle as mc
from tkinter import messagebox

class MohrStuff:

    def __init__(self):
        # Defining root
        page1 = tk.Toplevel()
        self.root = page1


        bg_img = tk.PhotoImage(file='blueprint_background.png')
        bg_label = tk.Label(self.root, image=bg_img)
        bg_label.place(x=0, y=0)

        # Change window size
        self.root.geometry('700x740')

        self.entry_frame = tk.Frame(self.root, )
        self.entry_frame.columnconfigure(0, weight=1)
        self.entry_frame.columnconfigure(1, weight=3)

        self.label_main = tk.Label(self.root, text="Mohr's Circle Stress Calculator", font='Arial, 25')
        self.label_sigmax = tk.Label(self.entry_frame, text='Sigma x: ', font=('Arial, 20'), )
        self.label_sigmay = tk.Label(self.entry_frame, text='Sigma y: ', font=('Arial, 20'))
        self.label_tauxy = tk.Label(self.entry_frame, text='Tau xy:', font=('Arial, 20'))
        self.label_units = tk.Label(self.entry_frame, text='Units:', font=('Arial, 20'))

        self.entry_sigmax = tk.Entry(self.entry_frame, width=10)
        self.entry_sigmay = tk.Entry(self.entry_frame, width=10)
        self.entry_tauxy = tk.Entry(self.entry_frame, width=10)

        self.button_calculate = tk.Button(self.entry_frame, text='Calculate', command=self.display_plot, fg='blue')

        self.slider_var = tk.IntVar()
        self.slider = tk.Scale(self.root, from_=0, to=360, length=300, tickinterval=45, orient='horizontal',
                               label='Angle', font=('Arial', 15), variable=self.slider_var, command=self.update_plot)

        # Creating option Menu
        self.options = ['Pa', 'Kpa', 'Mpa', 'Gpa', 'Psi', 'Psf', 'Ksi', 'Ksf']
        self.option_var = tk.StringVar(value=self.options[0])
        self.option_menu = tk.OptionMenu(self.entry_frame, self.option_var, *self.options, self.options[0])

        # Placing Labels on frame grid
        self.label_main.pack()
        self.label_sigmax.grid(row=0, column=0)
        self.label_sigmay.grid(row=1, column=0)
        self.label_tauxy.grid(row=2, column=0)

        # Placing Entry Boxes on frame grid
        self.entry_sigmax.grid(row=0, column=1, )
        self.entry_sigmay.grid(row=1, column=1)
        self.entry_tauxy.grid(row=2, column=1)

        self.option_menu.grid(row=3, column=1, sticky=tk.EW)

        self.button_calculate.grid(row=4, column=1)

        # Adding Canvas
        self.can1 = mc.FigureCanvasTkAgg()

        # Packing Entry and labels frame
        self.entry_frame.pack(padx=10, pady=10)
        self.root.mainloop()


        #Initilizing plot variables
        self.sigmax = 0
        self.sigmay = 0
        self.tauxy = 0

    def display_plot(self):
        self.can1.get_tk_widget().destroy()

        try:
            self.sigmax = float(self.entry_sigmax.get())
            self.sigmay = float(self.entry_sigmay.get())
            self.tauxy = float(self.entry_tauxy.get())

        except:
            tk.messagebox.showerror(title='TypeError', message="Please enter valid number values.")
            return None

        # Adds Slider
        self.slider.pack(side='top')

        # Adds Plot of Mohr's Circle onto canvas and packs
        m1 = mc.MohrsCircle(self.sigmax, self.sigmay, self.tauxy, units=self.option_var.get())
        canvas = mc.FigureCanvasTkAgg(m1.circle_plot(), master=self.root)
        self.can1 = canvas
        canvas.get_tk_widget().pack(side='bottom')

    def update_plot(self, angle):
        self.can1.get_tk_widget().destroy()
        m1 = mc.MohrsCircle(self.sigmax, self.sigmay, self.tauxy, units=self.option_var.get())
        canvas = mc.FigureCanvasTkAgg(m1.circle_plot(self.slider_var.get()), master=self.root)
        self.can1 = canvas
        canvas.get_tk_widget().pack(side='bottom')


if __name__ == '__main__':
    MohrStuff()
