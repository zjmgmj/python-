# -*- coding: utf-8 -*-
"""
@author: zhjm
"""
from splinter.browser import Browser
from time import sleep
#import traceback
#import time, sys
 
class huoche(object):
    """docstring for huoche"""
    driver_name=''
    executable_path=''
    #用户名，密码
    username = u"******"
    passwd = u"******"
    # cookies值得自己去找, 下面两个分别是常州, 蚌埠
    starts = u"%u5E38%u5DDE%2CCZH"
    ends = u"%u868C%u57E0%2CBBH"
    # 时间格式2018-01-19
    dtime = u"2018-02-12"
    # 车次，选择第几趟，0则从上之下依次点击
    order = 5
    ###乘客名
    users = [u"***",u"***"]
    ##席位
    xb = u"二等座"
    pz=u"成人票"
 
    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    buy="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    login_url='https://kyfw.12306.cn/otn/login/init'
     
    def __init__(self):
        self.driver_name='chrome'
        #self.executable_path='/chromedriver'
        #C:/Users/Administrator/AppData/Local/Google/Chrome/Application
 
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print (u"等待验证码，自行输入...")
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break
 
    def start(self):
        #self.driver=Browser(driver_name=self.driver_name,executable_path=self.executable_path)
        self.driver=Browser(driver_name=self.driver_name)
        self.driver.driver.set_window_size(1400, 1000)
        self.login()
        # sleep(1)
        self.driver.visit(self.ticket_url)
        try:
            print (u"购票页面开始...")
            sleep(1)
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
 
            self.driver.reload()
 
            count=0
            #print(self.order);
            if self.order!=0:
                while self.driver.url==self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print (u"循环点击查询... 第 %s 次" % count)
                    # sleep(1)
                    try:
                        self.driver.find_by_text(u"预订")[self.order - 1].click()
                        #print(self.order)
                    except Exception as e:
                        print (e)
                        print (u"还没开始预订")
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print (u"循环点击查询... 第 %s 次" % count)
                    sleep(1)
                    G1974=self.driver.find_by_id("ZE_5l000G197420").text
                    G1258=self.driver.find_by_id("ZE_5l000G125890").text
                    G1806=self.driver.find_by_id("ZE_5l000G180620").text
                    G1920=self.driver.find_by_id("ZE_5l000G192040").text
                    G116=self.driver.find_by_id("ZE_5l0000G11662").text
                    G1228=self.driver.find_by_id("ZE_5j000G122810").text
                    G1924=self.driver.find_by_id("ZE_5l000G192411").text
                    G4318=self.driver.find_by_id("ZE_5l000G431820").text
                    G216=self.driver.find_by_id("ZE_5l0000G21673").text
                    G158=self.driver.find_by_id("ZE_5l0000G158B5").text
                    G160=self.driver.find_by_id("ZE_5l0000G160U0").text
                    G7292=self.driver.find_by_id("ZE_55000G729230").text
                    """
                    ZE_5l000 G1258 90 
                    ZE_5l000G125890 G1258  10:08
                    ZE_5l000G180620 G1806  10:13
                    ZE_5l000G192040 G1920
                    ZE_5l0000G11662 G116
                    ZE_5j000G122810
                    ZE_5l000G192411
                    ZE_5l000G431820
                    ZE_5l0000G21673
                    ZE_5l0000G158B5
                    ZE_5l0000G160U0
                    ZE_55000G729230        18:46
                    """
                    if int(G1974)>2 or int(G1258)>2 or int(G1806)>2 or int(G1920)>2 or int(G116)>2 or int(G1228)>2 or int(G1924)>2 or int(G4318)>2 or int(G216)>2 or int(G158)>2 or int(G160)>2 or int(G7292)>2:
                        try:
                            print('1')
                            for i in self.driver.find_by_text(u"预订"):
                                try:
                                    i.click()
                                    #sleep(1)
                                except:
                                    continue
                        except Exception as e:
                            print (e)
                            print (u"还没开始预订 %s" %count)
                            continue
                    
            print (u"开始预订...")
            # sleep(3)
            # self.driver.reload()
            sleep(1)
            print (u'开始选择用户...')
            for user in self.users:
                self.driver.find_by_text(user).last.click()
 
            print (u"提交订单...")
            sleep(1)
            self.driver.find_by_text(self.pz).click()
            self.driver.find_by_id('').select(self.pz)
            sleep(1)
            self.driver.find_by_text(self.xb).click()
            sleep(1)
            """
            self.driver.find_by_id('submitOrder_id').click()
            print (u"开始选座...")
            self.driver.find_by_id('1D').last.click()
            self.driver.find_by_id('1F').last.click()

            sleep(1.5)
            print (u"确认选座...")
            """
            #self.driver.find_by_id('qr_submit_id').click()
 
        except Exception as e:
            print (e)
 
if __name__ == '__main__':
    huoche=huoche()
    huoche.start()