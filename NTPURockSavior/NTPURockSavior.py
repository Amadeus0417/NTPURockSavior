from Savior import NTPURockSavior
from SaviorData import SaviorData
from SaviorUI import SaviorUI
import Sheet
import time

#import pandas as pd
#import re, time, requests

savior = SaviorUI()

driver = NTPURockSavior()
driver.FaceBookLogin(savior.data.account, savior.data.password)
#savior.GetComments(data.website)
driver.GetComments("https://www.facebook.com/permalink.php?story_fbid=pfbid02ow2NDRJpiJ4hwZx5orxKiT8v5EA8S3HvZXGEFcB5PjkVvdp4vDnBaVULRLPCvFmql&id=100000304782470")
driver.LoadRentInfo()

sheet = Sheet(savior.data.gsjson)
sheet.OpenSheet(savior.data.gsheet)
sheet.ChooseWorkSheet(savior.data.wsheet)
sheet.FillData(driver.rentlist)





        
