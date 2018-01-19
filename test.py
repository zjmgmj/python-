# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:35:25 2018

@author: Administrator
"""

from splinter.browser import Browser
b = Browser(driver_name="chrome")



url = "https://kyfw.12306.cn/otn/leftTicket/init"
b.visit(url)
b.find_by_text(u"登录").click()

b.fill("loginUserDTO.user_name","943257156@qq.com")
b.fill("userDTO.password","zhjm520gmj620")
   

b.find_by_text(u"车票预订").click()
b.cookies.add({"_jc_save_fromStation":"%u5E38%u5DDE%2CCZH"})#出发站
b.cookies.add({"_jc_save_fromDate":"2018-02-12"})#出发时间
b.cookies.add({u'_jc_save_toStation':'%u868C%u57E0%2CBBH'})#到达站
b.reload()

b.find_by_text(u"查询").click()

"""
console中输入 autoSearchTime=5000
12306自动查询火车票
"""
b.find_by_text(u"预订")[0].click()




