import tkinter as tk

import numpy as np
from pint import UnitRegistry


class ConversionPage:
    def __init__(self):
        # Defines root attributes
        self.root = tk.Toplevel(bg='blue')

        # Places background image
        bg_img = tk.PhotoImage(file='blueprint_background.png')
        bg_label = tk.Label(self.root, image=bg_img)
        bg_label.place(x=0, y=0)
        # Defines Frame containers
        self.button_container = tk.Frame(self.root)
        self.entry_container = tk.Frame(self.root, bg='#1E3087')

        # Main Label
        self.label_main = tk.Label(self.root, text="Unit Conversion Calculator", font=('Arial', 20), fg='white',
                                   bg='#1E3087')

        # Category buttons
        button_temp = tk.Button(self.button_container, text='Temp',
                                command=lambda: self.create_entry(self.entry_container, category='temp'),
                                highlightbackground='#1E3087')
        button_length = tk.Button(self.button_container, text='Length', highlightbackground='#1E3087',
                                  command=lambda: self.create_entry(self.entry_container, category='length'))
        button_time = tk.Button(self.button_container, text='Time', highlightbackground='#1E3087',
                                command=lambda: self.create_entry(self.entry_container, category='time'))
        button_mass = tk.Button(self.button_container, text='Mass', highlightbackground='#1E3087',
                                command=lambda: self.create_entry(self.entry_container, category='mass'))
        button_custom = tk.Button(self.button_container, text='Custom', bg='blue', highlightbackground='#1E3087',
                                  command=lambda: self.create_entry(self.entry_container, category='custom'))

        self.buttons = [button_temp, button_length, button_time, button_mass, button_custom]
        [item.grid(row=0, column=index, sticky=tk.NSEW) for index, item in enumerate(self.buttons)]

        # Adds label and button container to page
        self.label_main.pack()
        self.button_container.pack(pady=10)

        self.root.mainloop()

        # Conversion Function

    def create_entry(self, master, category):
        # Prevents duplicated frame object
        for child in self.entry_container.winfo_children():
            child.destroy()
        e1 = EntryForum(master)
        getattr(e1, category)()


class EntryForum:
    def __init__(self, master):
        self.master = master

        # Tracing entry 1 variable for callback
        entr1_var = tk.StringVar()
        e1_trace = entr1_var.trace('w', lambda name, index, mode, e1=entr1_var: self.callback())

        # Creates entry box and answer label
        self.entry1 = tk.Entry(self.master, bg='black', highlightbackground='#1E3087', textvariable=entr1_var, width=15)

        self.label_answer = tk.Label(self.master, bg='grey', width=15)

        self.option1 = tk.StringVar()
        self.option2 = tk.StringVar()
        option1_trace = self.option1.trace('w', lambda name, index, mode, option1=self.option1: self.callback())
        option2_trace = self.option2.trace('w', lambda name, index, mode, option2=self.option1: self.callback())

        self.label_eq = tk.Label(self.master, text='=', font=('Arial', 20), bg='#1E3087')

        self.master.pack(pady=20, padx=10)

        self.entry1.grid(row=0, column=0, padx=5)
        self.label_eq.grid(row=0, column=2, padx=5)
        self.label_answer.grid(row=0, column=3, padx=5)

    def temp(self):
        options = ['°F', '°C', '°K', '°R']

        dropdown1 = tk.OptionMenu(self.master, self.option1, *options)
        dropdown2 = tk.OptionMenu(self.master, self.option2, *options)

        dropdown1.grid(row=0, column=1)
        dropdown2.grid(row=0, column=4)

    def length(self):
        options = ['lightyear', 'mile', 'yard', 'foot', 'inch', 'kilometer', 'hectometer',
                   'meter', 'decimeter', 'centimeter', 'millimeter', 'micrometer', 'nanometer']

        dropdown1 = tk.OptionMenu(self.master, self.option1, *options)
        dropdown2 = tk.OptionMenu(self.master, self.option2, *options)

        dropdown1.grid(row=0, column=1)
        dropdown2.grid(row=0, column=4)

    def time(self):
        options = ['millennium', 'century', 'decade', 'year', 'month', 'week', 'day', 'hour', 'minute', 'second',
                   'millisecond', 'microsecond', 'nanosecond']

        dropdown1 = tk.OptionMenu(self.master, self.option1, *options)
        dropdown2 = tk.OptionMenu(self.master, self.option2, *options)

        dropdown1.grid(row=0, column=1)
        dropdown2.grid(row=0, column=4)
        self.master.pack(pady=20, padx=10)

    def mass(self):
        options = ['ton', 'kilopound', 'pound', 'tonne', 'kilogram', 'gram', 'milligram', 'microgram', 'nanogram']

        dropdown1 = tk.OptionMenu(self.master, self.option1, *options)
        dropdown2 = tk.OptionMenu(self.master, self.option2, *options)

        dropdown1.grid(row=0, column=1)
        dropdown2.grid(row=0, column=4)

    def custom(self):
        label_entry = tk.Label(self.master, text='Value', bg='#1E3087')
        label_units1 = tk.Label(self.master, text='Units', bg='#1E3087')
        label_units2 = tk.Label(self.master, text='Units', bg='#1E3087')

        units_textbox = tk.Entry(self.master, bg='black', highlightbackground='#1E3087', textvariable=self.option1,
                                 width=10)
        units_textbox2 = tk.Entry(self.master, bg='black', highlightbackground='#1E3087', textvariable=self.option2,
                                  width=10)

        self.entry1.grid(row=1, column=0)
        self.label_eq.grid(row=1, column=3)
        self.label_answer.grid(row=1, column=4)

        label_entry.grid(row=0, column=0)
        label_units1.grid(row=0, column=1)
        label_units2.grid(row=0, column=5)

        units_textbox.grid(row=1, column=1)
        units_textbox2.grid(row=1, column=5)

    @staticmethod
    def convert(value, unit0, unit1):
        """
        Converts Given value in starting units to ending units

        :param value:
        :param unit0:
        :param unit1:
        :return:
        """

        ureg = UnitRegistry()
        try:
            value = float(value)
        except:
            if not value:
                return 0
            else:
                return np.NAN

        try:
            to_convert = ureg.Quantity(value, ureg[unit0])
            converted = to_convert.to(ureg[unit1])
            return format(converted.magnitude, '.5g')

        except:
            return value

    def callback(self):
        """
          Updates Answer textbox based on tracked entry box strvar

        :return:
        """
        answer = self.convert(self.entry1.get(), self.option1.get(), self.option2.get())
        self.label_answer.config(text=answer)


if __name__ == "__main__":
    c1 = ConversionPage()
