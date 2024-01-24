from datetime import datetime
from lib2to3.pgen2.parse import ParseError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class RentInfo:

    def __init__(self, date, timeStart, timeEnd, member):
        self.date = date
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.member = member

class NTPURockSavior:

    # set webdriver
    def __init__(self):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        self.rentlist = []
    # facebook login
    def FaceBookLogin(self, account, password):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.ID, "email").send_keys(account)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.find_element(By.NAME, 'login').click()
    # expand comments
    def ExpandComments(self):
        while True:
            try:
                self.driver.find_element(By.CLASS_NAME, "x78zum5.x1w0mnb.xeuugli").click()
            except:
                break

        while True:
            try:
                self.driver.find_element(By.CLASS_NAME, "x1i10hfl.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1a2a7pz.x6s0dn4.xi81zsa.x1iyjqo2.xs83m0k.xsyo7zv.xt0b8zv").click()
            except:
                break
    # get comments
    def GetComments(self, postlink):
        self.driver.get(postlink)
        self.ExpandComments()
        self.comments = self.driver.find_elements(By.CLASS_NAME, "xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs")
        
    # 分割租借資訊到 rentinfo 物件內(可以用 pd.dataframe 改寫)
    def LoadRentInfo(self):
        self.rentlist = []
        for c in self.comments:
            commentinfo = c.text.split(' ')
            if(commentinfo[0] == '#'):
                self.rentlist.clear()
                continue;
            try:
                date = datetime.strptime(commentinfo[0], '%m/%d').day
                time = commentinfo[1].split('-')
                timeStart = datetime.strptime(self.fourdigit(time[0]), '%H%M')
                timeEnd = datetime.strptime(self.fourdigit(time[1]), '%H%M')
                member = '\n'.join(commentinfo[2:])
                self.rentlist.append(RentInfo(date, timeStart, timeEnd, member))
            except (ParseError, ValueError):
                pass

    def fourdigit(self, t):
        if len(t) == 1:
            t = '0' + t + '00'
        elif len(t) == 2:
            t = t + '00'
        elif len(t) == 3:
            t = '0' + t
        return t