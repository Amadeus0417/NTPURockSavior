import tkinter as tk

class SaviorData:
    
    def __init__(self):
        self.account = tk.StringVar()
        self.password = tk.StringVar()
        self.website = tk.StringVar()
        self.gsheet = tk.StringVar()
        self.wsheet = tk.StringVar()
        self.hsheet = tk.StringVar()
        self.hwsheet = tk.StringVar()
        self.isCal = tk.BooleanVar()
        self.isFill = tk.BooleanVar()