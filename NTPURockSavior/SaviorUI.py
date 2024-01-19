#-*- coding: big5 -*-

import os
import os.path
import tkinter as tk
import SaviorData

class SaviorUI:
    
    def __init__(self, data):
        self.window = tk.Tk()
        self.window.title('NTPU Rock Helper')
        self.window.geometry("800x600")
        tk.Label(self.window, text= 'Facebook 帳號').grid(row=0, column=0)
        tk.Label(self.window, text= 'Facebook 密碼').grid(row=1, column=0)
        tk.Label(self.window, text= '租借表貼文網址').grid(row=2, column=0)
        tk.Label(self.window, text= '社辦租借表連結').grid(row=3, column=0)
        tk.Label(self.window, text= '租借工作表名稱').grid(row=4, column=0)
        tk.Label(self.window, text='練團時數統計表連結').grid(row=5, column=0)
        tk.Label(self.window, text='統計工作表名稱').grid(row=6,  column=0)
        tk.Label(self.window, text='json 憑證檔案位置').grid(row=7,  column=0)
        tk.Entry(self.window, textvariable=data.account).grid(row=0, column=1)
        tk.Entry(self.window, textvariable=data.password).grid(row=1, column=1)
        tk.Entry(self.window, textvariable=data.website).grid(row=2, column=1)
        tk.Entry(self.window, textvariable=data.gsheet).grid(row=3, column=1)
        tk.Entry(self.window, textvariable=data.wsheet).grid(row=4, column=1)
        tk.Entry(self.window, textvariable=data.hsheet).grid(row=5, column=1)
        tk.Entry(self.window, textvariable=data.hwsheet).grid(row=6, column=1)
        tk.Entry(self.window, textvariable=data.gsjson).grid(row=7, column=1)
        tk.Button(self.window, text='確認', command=self.window.destroy).grid(row=8, column=0, columnspan=2)
        try:
            self.AutoFill(data)
        except:
            pass
        self.window.mainloop()
        self.Memorize()


    def AutoFill(self, data):
        self.path = os.getenv('temp')
        self.filename = os.path.join(self.path, 'info.txt')
        try:
            with open(self.filename) as fp:
                acc, pas, web, gsh, wsh, hsh, hws, gsj = fp.read().strip().split(',')
                data.account.set(acc)
                data.password.set(pas)
                data.website.set(web)
                data.gsheet.set(gsh)
                data.wsheet.set(wsh)
                data.hsheet.set(hsh)
                data.hwsheet.set(hws)
                data.gsjson.set(gsj)
        except:
            pass

    def Memorize(self, data):
        with open(self.filename, 'w') as fp:
            fp.write(','.join((data.account.get(),
                               data.password.get(), 
                               data.website.get(), 
                               data.gsheet.get(), 
                               data.wsheet.get(), 
                               data.hsheet.get(), 
                               data.hwsheet.get(), 
                               data.gsjson.get())))