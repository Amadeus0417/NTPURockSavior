from Savior import NTPURockSavior
from SaviorData import SaviorData
from SaviorUI import SaviorUI
from Sheet import Sheet
import time

#import pandas as pd
#import re, time, requests

savior_UI = SaviorUI()
sheet = Sheet(savior_UI.data.gsjson.get())

if(savior_UI.data.isFill.get()):
    savior = NTPURockSavior()
    savior.FaceBookLogin(savior_UI.data.account.get(), savior_UI.data.password.get())
    savior.GetComments(savior_UI.data.website.get())
    savior.LoadRentInfo()
    sheet.OpenWorkSheet(savior_UI.data.gsheet.get(), savior_UI.data.wsheet.get())
    sheet.FillData(savior.rentlist)
 
if(savior_UI.data.isCal.get()):
    sheet.OpenWorkSheet(savior_UI.data.gsheet.get(), savior_UI.data.wsheet.get())
    sheet.OpenStatSheet(savior_UI.data.hsheet.get(), savior_UI.data.hwsheet.get())
    sheet.Calculate()




        
