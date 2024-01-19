#-*- coding: big5 -*-

import os
import os.path
import tkinter as tk
from SaviorData import SaviorData

class SaviorUI:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('NTPU Rock Helper')
        self.window.geometry("800x600")
        self.data = SaviorData()
        tk.Label(self.window, text= 'Facebook �b��').grid(row=0, column=0)
        tk.Label(self.window, text= 'Facebook �K�X').grid(row=1, column=0)
        tk.Label(self.window, text= '���ɪ�K����}').grid(row=2, column=0)
        tk.Label(self.window, text= '���쯲�ɪ�s��').grid(row=3, column=0)
        tk.Label(self.window, text= '���ɤu�@��W��').grid(row=4, column=0)
        tk.Label(self.window, text='�m�ήɼƲέp��s��').grid(row=5, column=0)
        tk.Label(self.window, text='�έp�u�@��W��').grid(row=6,  column=0)
        tk.Label(self.window, text='json �����ɮצ�m').grid(row=7,  column=0)
        tk.Entry(self.window, textvariable=self.data.account).grid(row=0, column=1)
        tk.Entry(self.window, textvariable=self.data.password).grid(row=1, column=1)
        tk.Entry(self.window, textvariable=self.data.website).grid(row=2, column=1)
        tk.Entry(self.window, textvariable=self.data.gsheet).grid(row=3, column=1)
        tk.Entry(self.window, textvariable=self.data.wsheet).grid(row=4, column=1)
        tk.Entry(self.window, textvariable=self.data.hsheet).grid(row=5, column=1)
        tk.Entry(self.window, textvariable=self.data.hwsheet).grid(row=6, column=1)
        tk.Entry(self.window, textvariable=self.data.gsjson).grid(row=7, column=1)
        tk.Button(self.window, text='�T�{', command=self.window.destroy).grid(row=8, column=0, columnspan=2)
        try:
            self.AutoFill()
        except:
            pass
        self.window.mainloop()
        self.Memorize()


    def AutoFill(self):
        self.path = os.getenv('temp')
        self.filename = os.path.join(self.path, 'info.txt')
        try:
            with open(self.filename) as fp:
                acc, pas, web, gsh, wsh, hsh, hws, gsj = fp.read().strip().split(',')
                self.data.account.set(acc)
                self.data.password.set(pas)
                self.data.website.set(web)
                self.data.gsheet.set(gsh)
                self.data.wsheet.set(wsh)
                self.data.hsheet.set(hsh)
                self.data.hwsheet.set(hws)
                self.data.gsjson.set(gsj)
        except:
            pass

    def Memorize(self):
        with open(self.filename, 'w') as fp:
            fp.write(','.join((self.data.account.get(),
                               self.data.password.get(), 
                               self.data.website.get(), 
                               self.data.gsheet.get(), 
                               self.data.wsheet.get(), 
                               self.data.hsheet.get(), 
                               self.data.hwsheet.get(), 
                               self.data.gsjson.get())))