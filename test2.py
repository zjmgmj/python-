# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:07:59 2018

@author: Administrator
"""

from splinter.browser import Browser
from time import sleep

class test(object):
    driver_name=''
    executable_path=''
    #用户名，密码
    username = u"943257156@qq.com"
    passwd = u"zhjm520gmj620"
    # cookies值得自己去找, 下面两个分别是上海, 太原南
    starts = u"%u5E38%u5DDE%2CCZH"
    ends = u"%u868C%u57E0%2CBBH"
    # 时间格式2018-01-19
    dtime = u"2018-01-26"
    # 车次，选择第几趟，0则从上之下依次点击
    order = 0
    ###乘客名
    users = [u"郑家敏",u"宫明娟"]
    ##席位
    xb = u"二等座"
    pz=u"成人票"
 
    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    #login_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    buy="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    #login_url='https://kyfw.12306.cn/otn/login/init'
    
    def __init__(self):
        self.driver_name='chrome'
    
    
    def start(self):
        self.driver=Browser(driver_name=self.driver_name)
        self.driver.driver.set_window_size(1400, 1000)
        
        self.driver.visit(self.login_url)
        
        sleep(1)
        self.driver.find_by_text(u"车票预订").click()
        sleep(1)
        
        self.driver.cookies.add({"_jc_save_fromStation": self.starts})
        self.driver.cookies.add({"_jc_save_toStation": self.ends})
        self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
        self.driver.reload()
        
        self.driver.find_by_text(u"查询").click()
        
        self.driver.find_by_tag
        print(self.driver.find_by_id("ticket_5l0000G45640").pop().text)
        """
        ZE_5l0000G45640=self.driver.find_by_id("ZE_5l0000G45640").text
        
        if int(ZE_5l0000G45640)>2:
           print('111')
        """
        
        



if __name__ == '__main__':
    test=test()
    test.start()