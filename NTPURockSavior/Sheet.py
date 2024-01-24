#-*- coding: big5 -*-

import pygsheets
import re
import pandas as pd
import calendar
from datetime import datetime

class Sheet:
    #���ogoogle�����v
    def __init__(self, token):
        self.gc = pygsheets.authorize(service_account_file=token)
    #�}�Ҹպ��
    def OpenWorkSheet(self, link, name):
        self.ws = self.gc.open_by_url(link).worksheet_by_title(name)
    def OpenStatSheet(self, link, name):
        self.statSheet = self.gc.open_by_url(link).worksheet_by_title(name)
    #�}�ҫ��w�u�@��
    def is_cell_empty(self, a, b, col) -> bool:
        while a <= b:
            if(self.ws.get_value((a, col)) != ''):
                return False
            a+=1
        return True
    def SetDataFrame(self, data):
        self.df = pd.DataFrame(data)
        month = calendar.monthrange(datetime.now().year, datetime.now().month)
        year = str(datetime.now().year) + '/'
        first = str(datetime.now().month) + '/1'
        last = str(datetime.now().month) + '/' + str(month[1])
        date = pd.date_range(start=year+first, end=year+last, freq="D").strftime('%m/%d')
        self.df.columns = date
    #��J���
    def FillData(self, rentlist):
        data = [['' for c in range(31)] for r in range(48)]
        for e in rentlist:
            RowStart = int((e.timeStart.hour + (e.timeStart.minute / 60)) * 2 + 2)
            RowEnd = int((e.timeEnd.hour + (e.timeEnd.minute / 60)) * 2 + 1)
            Col = e.date + 1
            if(self.is_cell_empty(RowStart, RowEnd, Col) == False):
                continue
            self.ws.merge_cells(start=(RowStart, Col), end=(RowEnd, Col))
            data[RowStart-2][Col-2] = e.member
            #self.ws.update_value((RowStart, Col), e.member)
        self.SetDataFrame(data)
        self.ws.set_dataframe(self.df, (1,2))
    #�p��m�ήɼ�(Ū���x�s�椺��data�B���ΡB�A�����ɼ�)
    def Calculate(self):
        stat = dict()
        grange = self.ws.merged_ranges
        for r in grange:
            col = r.start.col
            start = r.start.row
            end = r.end.row
            member = re.split('[\n\s]', self.ws.get_value((start, col)))
            for m in member:
                try:
                    stat[m] += (end - start + 1) * 0.5
                except:
                    stat[m] = (end - start + 1) * 0.5
        statMatrix = pd.DataFrame(list(stat.items()))
        statMatrix.columns = ['�m�W', '�m�ήɼ�']
        self.statSheet.set_dataframe(statMatrix, (1,1))
        
        