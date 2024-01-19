from Savior import NTPURockSavior
from SaviorData import SaviorData
from SaviorUI import SaviorUI
import Sheet
import time

#import pandas as pd
#import re, time, requests
data = SaviorData()

window = SaviorUI(data)

savior = NTPURockSavior()
savior.FaceBookLogin(data.account, data.password)
#savior.GetComments(data.website)
savior.GetComments("https://www.facebook.com/permalink.php?story_fbid=pfbid02ow2NDRJpiJ4hwZx5orxKiT8v5EA8S3HvZXGEFcB5PjkVvdp4vDnBaVULRLPCvFmql&id=100000304782470")
savior.LoadRentInfo()

sheet = Sheet(data.gsjson)
sheet.OpenSheet(data.gsheet)
sheet.ChooseWorkSheet(data.wsheet)
sheet.FillData(savior.rentlist)





        
