import pygsheets

class Sheet:
    #取得google表單授權
    def __init__(self, token):
        self.gc = pygsheets.authorize(service_account_file=token)
    #開啟試算表
    def OpenSheet(self, link):
        self.sheet = self.gc.open_by_url(link)
    #開啟指定工作表
    def ChooseWorkSheet(self, name):
        self.ws = self.sheet.worksheet_by_title(name)
    def is_cell_empty(self, a, b, col) -> bool:
        while a <= b:
            if(self.ws.get_value((a, col)) != ''):
                return False
            a+=1
        return True
    #填入資料
    def FillData(self, rentlist):
        for e in rentlist:
            RowStart = int((e.timeStart.hour + (e.timeStart.minute / 60)) * 2 + 2)
            RowEnd = int((e.timeEnd.hour + (e.timeEnd.minute / 60)) * 2 + 1)
            Col = e.date + 1
            if(self.is_cell_empty(RowStart, RowEnd, Col) == False):
                continue
            self.ws.merge_cells(start=(RowStart, Col), end=(RowEnd, Col))
            self.ws.update_value((RowStart, Col), e.member)

    def Stats(self, rentlist):
        return
        