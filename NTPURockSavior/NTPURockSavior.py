from Savior import NTPURockSavior
from SaviorUI import SaviorUI
import Sheet
import time

#import pandas as pd
#import re, time, requests

window = SaviorUI()

savior = NTPURockSavior()
savior.FaceBookLogin("oscar83155@gmail.com", "amadeus0417")
savior.GetComments("https://www.facebook.com/permalink.php?story_fbid=pfbid02ow2NDRJpiJ4hwZx5orxKiT8v5EA8S3HvZXGEFcB5PjkVvdp4vDnBaVULRLPCvFmql&id=100000304782470")
time.sleep(5)
#savior.GetComments("https://www.facebook.com/groups/183236594717256/posts/282242764816638/")
savior.LoadRentInfo()

sheet = Sheet("C:\\Users\oscar\\source\\repos\\Amadeus0417\\NTPURockSavior\\NTPURockSavior\\ntpu-rock-helper.json")
sheet.OpenSheet("https://docs.google.com/spreadsheets/d/1xXQ2xZev1V2alaQ2T_FBnJrjCJgbugxs2GhMoCCzu6s/edit#gid=0")
sheet.ChooseWorkSheet("工作表1")
sheet.FillData(savior.rentlist)





        
