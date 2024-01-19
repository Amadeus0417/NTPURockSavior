from Savior import NTPURockSavior
from SaviorData import SaviorData
from SaviorUI import SaviorUI
import Sheet
import time

#import pandas as pd
#import re, time, requests

savior_UI = SaviorUI()

savior = NTPURockSavior()
savior.FaceBookLogin(savior_UI.data.account, savior_UI.data.password)
#savior.GetComments(data.website)
savior.GetComments("https://www.facebook.com/permalink.php?story_fbid=pfbid02ow2NDRJpiJ4hwZx5orxKiT8v5EA8S3HvZXGEFcB5PjkVvdp4vDnBaVULRLPCvFmql&id=100000304782470")
savior.LoadRentInfo()

sheet = Sheet(savior_UI.data.gsjson)
sheet.OpenSheet(savior_UI.data.gsheet)
sheet.ChooseWorkSheet(savior_UI.data.wsheet)
sheet.FillData(savior.rentlist)





        
