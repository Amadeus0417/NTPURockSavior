from msilib.schema import SelfReg
import os
import os.path
import tkinter as tk

class SaviorUI:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('NTPU Rock Helper')
        self.window.geometry("800x600")
        self.account = tk.StringVar()
        self.password = tk.StringVar()
        self.website = tk.StringVar()
        self.gsheet = tk.StringVar()
        self.wsheet = tk.StringVar()
        self.hsheet = tk.StringVar()
        self.hwsheet = tk.StringVar()
        self.gsjson = tk.StringVar()
        tk.Label(self.window, text= 'Facebook �b��').grid(row=0, column=0)
        tk.Label(self.window, text= 'Facebook �K�X').grid(row=1, column=0)
        tk.Label(self.window, text= '���ɪ�K����}').grid(row=2, column=0)
        tk.Label(self.window, text= '���쯲�ɪ�s��').grid(row=3, column=0)
        tk.Label(self.window, text= '���ɤu�@��W��').grid(row=4, column=0)
        tk.Label(self.window, text='�m�ήɼƲέp��s��').grid(row=5, column=0)
        tk.Label(self.window, text='�έp�u�@��W��').grid(row=6,  column=0)
        tk.Label(self.window, text='json �����ɮצ�m').grid(row=7,  column=0)
        tk.Entry(self.window, textvariable=self.account).grid(row=0, column=1)
        tk.Entry(self.window, textvariable=self.password).grid(row=1, column=1)
        tk.Entry(self.window, textvariable=self.website).grid(row=2, column=1)
        tk.Entry(self.window, textvariable=self.gsheet).grid(row=3, column=1)
        tk.Entry(self.window, textvariable=self.wsheet).grid(row=4, column=1)
        tk.Entry(self.window, textvariable=self.hsheet).grid(row=5, column=1)
        tk.Entry(self.window, textvariable=self.hwsheet).grid(row=6, column=1)
        tk.Entry(self.window, textvariable=self.gsjson).grid(row=7, column=1)
        tk.Button(self.window, text='�T�{', command=self.window.destroy).grid(row=8, column=0, columnspan=2)