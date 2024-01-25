from Savior import NTPURockSavior
from SaviorData import SaviorData
from SaviorUI import SaviorUI
from Sheet import Sheet
import time

savior_UI = SaviorUI()
credentialPath = './ntpu-rock-helper.json'
sheet = Sheet(credentialPath)

if(savior_UI.data.isFill.get()):
    savior = NTPURockSavior()
    savior.FaceBookLogin(savior_UI.data.account.get(), savior_UI.data.password.get())
    print('Loading comments...')
    savior.GetComments(savior_UI.data.website.get())
    time.sleep(5)
    savior.LoadRentInfo()
    time.sleep(5)
    print('Loading completed. Filling data...')
    sheet.OpenWorkSheet(savior_UI.data.gsheet.get(), savior_UI.data.wsheet.get())
    sheet.FillData(savior.rentlist)
    print('Data filled successfully!')
 
if(savior_UI.data.isCal.get()):
    print('Calculating stats...')
    sheet.OpenWorkSheet(savior_UI.data.gsheet.get(), savior_UI.data.wsheet.get())
    sheet.OpenStatSheet(savior_UI.data.hsheet.get(), savior_UI.data.hwsheet.get())
    sheet.Calculate()
    print('Calculate completed!')




        
