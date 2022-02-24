import tkinter as tk
from tkinter import ttk
import sys

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("{}x{}".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.resizable(False, False)
        self.title("Metre-Feet converter")
        self.columnconfigure(0, weight=1)

        container = tk.Frame(self, padx=15, pady=10)
        container.grid()

        feetToMetreFrame = FeetToMetreFrame(container, self)
        metreToFeetFrame = MetresToFeetFrame(container, self)
        self.frames = dict()
        self.frames[FeetToMetreFrame] = feetToMetreFrame
        self.frames[MetresToFeetFrame] = metreToFeetFrame
        feetToMetreFrame.grid(column=0, row=0)
        metreToFeetFrame.grid(column=0, row=0)

        self.bind("q", sys.exit)
        self.bind("<Return>", metreToFeetFrame.calculate)
        self.bind("<KP_Enter>", metreToFeetFrame.calculate)

    def swapFrame(self, key):
        frame = self.frames[key]
        frame.tkraise()
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)

class MetresToFeetFrame(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.configure(padx=15, pady=10)
        self.root = root
        #self.frame = ttk.Frame(self.root, padding=(15,10))
        #self.frame.grid(column=0, row=0)

        self.feetConverted = tk.StringVar()

        self.metreLabel = ttk.Label(self, text="Metres")
        self.metreEntry = ttk.Entry(self)
        self.feetLabel = ttk.Label(self, text="Feet")
        self.feetFinallabel = ttk.Label(self, textvariable=self.feetConverted, width=20, font=("Segoi-UI",15))
        self.calculateButton = ttk.Button(self, text="Calculate", command=self.calculate)
        self.swapButton = ttk.Button(self, text="Change to feet-to-metre", command=lambda:root.swapFrame(FeetToMetreFrame))

        self.metreLabel.grid(column=0, row=0, padx=15, pady=10, sticky="EW")
        self.metreEntry.grid(column=1, row=0, padx=15, pady=10, sticky="EW")
        self.feetLabel.grid(column=0, row=1, padx=15, pady=10,sticky="EW")
        self.feetFinallabel.grid(column=1, row=1, padx=25, pady=10, sticky="EW")
        self.calculateButton.grid(column=0, row=2, padx=25, pady=10, columnspan=2, sticky="EW")
        self.swapButton.grid(column=0, row=3, padx=30, pady=10, columnspan=2, sticky="EW")

        self.metreEntry.focus()
        #self.bind("<Return>", self.calculate)

    def calculate(self, *args, **kwargs):
        self.feetConverted.set(3.28084*int(self.metreEntry.get()))

class FeetToMetreFrame(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.configure(padx=15, pady=10)
        self.root = root

        #self.frame = ttk.Frame(self.root, padding=(15,10))
        #self.frame.grid(column=0, row=0)

        self.feetConverted = tk.StringVar()

        self.feetLabel = ttk.Label(self, text="Feet")
        self.feetEntry = ttk.Entry(self)
        self.metreLabel = ttk.Label(self, text="Metres")
        self.metreFinallabel = ttk.Label(self, textvariable=self.feetConverted, width=20, font=("Segoi-UI",15))
        self.calculateButton = ttk.Button(self, text="Calculate", command=self.calculate)
        self.swapButton = ttk.Button(self, text="Change to metre-to-feet", command=lambda:self.root.swapFrame(MetresToFeetFrame))

        self.feetLabel.grid(column=0, row=0, padx=15, pady=10, sticky="EW")
        self.feetEntry.grid(column=1, row=0, padx=15, pady=10, sticky="EW")
        self.metreLabel.grid(column=0, row=1, padx=15, pady=10,sticky="EW")
        self.metreFinallabel.grid(column=1, row=1, padx=25, pady=10, sticky="EW")
        self.calculateButton.grid(column=0, row=2, padx=25, pady=10, columnspan=2, sticky="EW")
        self.swapButton.grid(column=0, row=3, padx=30, pady=10, columnspan=2, sticky="EW")

        self.feetEntry.focus()

    def calculate(self, *args, **kwargs):
        self.feetConverted.set(int(self.feetEntry.get())/3.28084)


root = Root()
#metreToFeetFrame = MetresToFeetFrame(root)
#feetToMetreFrame = FeetToMetreFrame(root)
root.mainloop()