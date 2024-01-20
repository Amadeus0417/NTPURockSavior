from Savior import NTPURockSavior
from SaviorData import SaviorData
from SaviorUI import SaviorUI
from Sheet import Sheet
import time

#import pandas as pd
#import re, time, requests

savior_UI = SaviorUI()

savior = NTPURockSavior()
savior.FaceBookLogin(savior_UI.data.account.get(), savior_UI.data.password.get())
savior.GetComments(savior_UI.data.website.get())
savior.LoadRentInfo()

sheet = Sheet(savior_UI.data.gsjson.get())
sheet.OpenSheet(savior_UI.data.gsheet.get())
sheet.ChooseWorkSheet(savior_UI.data.wsheet.get())
sheet.FillData(savior.rentlist)





        
