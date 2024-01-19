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
        tk.Label(self.window, text= 'Facebook 帳號').grid(row=0, column=0)
        tk.Label(self.window, text= 'Facebook 密碼').grid(row=1, column=0)
        tk.Label(self.window, text= '租借表貼文網址').grid(row=2, column=0)
        tk.Label(self.window, text= '社辦租借表連結').grid(row=3, column=0)
        tk.Label(self.window, text= '租借工作表名稱').grid(row=4, column=0)
        tk.Label(self.window, text='練團時數統計表連結').grid(row=5, column=0)
        tk.Label(self.window, text='統計工作表名稱').grid(row=6,  column=0)
        tk.Label(self.window, text='json 憑證檔案位置').grid(row=7,  column=0)
        tk.Entry(self.window, textvariable=self.account).grid(row=0, column=1)
        tk.Entry(self.window, textvariable=self.password).grid(row=1, column=1)
        tk.Entry(self.window, textvariable=self.website).grid(row=2, column=1)
        tk.Entry(self.window, textvariable=self.gsheet).grid(row=3, column=1)
        tk.Entry(self.window, textvariable=self.wsheet).grid(row=4, column=1)
        tk.Entry(self.window, textvariable=self.hsheet).grid(row=5, column=1)
        tk.Entry(self.window, textvariable=self.hwsheet).grid(row=6, column=1)
        tk.Entry(self.window, textvariable=self.gsjson).grid(row=7, column=1)
        tk.Button(self.window, text='確認', command=self.window.destroy).grid(row=8, column=0, columnspan=2)
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
                self.account.set(acc)
                self.password.set(pas)
                self.website.set(web)
                self.gsheet.set(gsh)
                self.wsheet.set(wsh)
                self.hsheet.set(hsh)
                self.hwsheet.set(hws)
                self.gsjson.set(gsj)
        except:
            pass

    def Memorize(self):
        with open(self.filename, 'w') as fp:
            fp.write(','.join((self.account.get(),
                               self.password.get(), 
                               self.website.get(), 
                               self.gsheet.get(), 
                               self.wsheet.get(), 
                               self.hsheet.get(), 
                               self.hwsheet.get(), 
                               self.gsjson.get())))