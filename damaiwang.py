# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import random
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import time
# import sys
# sys.path.append(r'/Users/kenny/Documents')
#
# #这是大麦网登录所要post的种类{"osType":4,"td_SMSVcode":"","mobilePrefix":"86","source":10188,"pwd":"asdfasdf","version":"60000","td_token":"damai-1520692302468-0.ad8d57d93f5be","account":"13402160763","phoneModels":"","sign":"","timestamp":1520692328134,"systemVersion":"","appType":"","clientGUID":"","appClientKey":""}
# #Message: {"errorMessage":"Element is not currently interactable and may not be manipulated","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Connection":"close","Content-Length":"102","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:62414","User-Agent":"Python-urllib/3.6"},"httpVersion":"1.1","method":"POST","post":"{\"value\": [\"\\ue007\"], \"id\": \":wdc:1520693855183\", \"sessionId\": \"58b5d270-2473-11e8-ad4d-3f33efb149c1\"}","url":"/value","urlParsed":{"anchor":"","query":"","file":"value","directory":"/","path":"/value","relative":"/value","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/value","queryKey":{},"chunks":["value"]},"urlOriginal":"/session/58b5d270-2473-11e8-ad4d-3f33efb149c1/element/:wdc:1520693855183/value"}}
# #Screenshot: available via screen
#
#
# from defphantomjs import start_browser
# from get_loging import login_web
#
# driver = login_web(logurl = 'https://m.damai.cn/damai/login/index.html?returnUrl=%2F%2Fm.damai.cn%2Fdamai%2Fhome%2Findex.html%23%2F#passwordLogin',
#                    username='13402160763',password='kennyming1941',usernamexpath='//input[@placeholder="请输入手机号"]',
#                    passwordxpath='//input[@placeholder="请输入密码"]',enter_xpath='//div[@class="password-login"]//div[@data-v-0a74c44e=""]')
#
# time.sleep(2)
# driver.save_screenshot('new.jpg')
# with open('cook.text','w') as f:
#     f.write(str(driver.get_cookies()))
# driver.quit()

#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url = 'https://secure.damai.cn/login.aspx?ru=https://www.damai.cn/sh/')
driver.find_element_by_xpath('//input[@id="login_email"]').send_keys('13402160763')  #输入用户名
driver.find_element_by_xpath('//div[@class="account_inner"]/input[@value="登录密码"]').send_keys('kennyming1941')  #密码
driver.find_element_by_xpath('//input[@class="login_btn"]').click() #点击登录
#driver.find_element_by_xpath('//div[@class="home_top"]//span[@[@class="home-top__city__cityname"]').click()
driver.find_element_by_xpath('//div[@class="search-main"]//input[@type="text"]').send_keys('王力宏') #进入搜索框输入
driver.find_element_by_xpath('//div[@class="search-main"]//input[@type="text"]').send_keys(Keys.ENTER) #回车
driver.find_element_by_xpath('//div[@class="search_txt"]//a[@onclick="toItem(140346,1,1,王力宏“龙的传人2060“巡回演唱会)"]').click() #点击搜索结果


# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.implicitly_wait(3)
# logurl = 'https://m.damai.cn/damai/login/index.html?returnUrl=%2F%2Fm.damai.cn%2Fdamai%2Fhome%2Findex.html%23%2F#passwordLogin'
# driver.get(url=logurl)
# driver.find_element_by_xpath('//input[@placeholder="请输入手机号"]').send_keys('13402160763')  #输入用户名
# driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('kennyming1941')  #密码
# driver.find_element_by_xpath('//div[@class="password-login"]//div[@data-v-0a74c44e=""]').click() #点击登录
#
#
# driver.find_element_by_xpath('//div[@class="my-bd__want"]//div[@class="title"]').click() #点击我想看的
# driver.find_element_by_xpath('//div[@class="like-list"]//div[@class="project-item_pic"]//img[@lazy="loaded"]').click() #点击我收藏的第一个
# driver.find_element_by_xpath('//div[@class="button-group__btn1"]//div[@class="dm-button dm-button__primary dm-button__large"]').click() #选择购买按键
# driver.find_element_by_xpath('//div[@class="dm-popup buy-popup buy-popup__box dm-popup-bottom"]//div[@class="dm-button dm-button__primary dm-button__large"]').click() #选择选择按键

