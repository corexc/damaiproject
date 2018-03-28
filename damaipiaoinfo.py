import requests
import pymongo
import time

con = pymongo.MongoClient('192.168.1.188'),32772
piaowuinfo = con.piaowuinfo
damai = piaowuinfo.damai

pull_time = time.strftime("%Y%m%d%X", time.localtime())
fist_page = 1

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': ' gzip, deflate, br', 'Accept-Language': ' zh-CN,zh;q=0.9', 'Connection': 'keep-alive', 'Content-Length': '65', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': 'x_hm_tuid=ZjljZbgGP7khUbpuSnnXZAK9evK0OON2V9FpyqKEBe30v2mQnN+NJQSn6nxmUTvM; damai_login_QRCode=f5fd7254-134d-499d-88c4-7783017677f2; UM_distinctid=1626592db812d3-029871ed0ccafd-33697b04-384000-1626592db82362; damai_t_l_b="RUHviFL8YXPWp2vrLfQyoKdKOGeqWym20rg3T4nsLuYbFvb5GO6qKA=="; damai_ams=X6PCWlebN7YbFvb5GO6qKA%3D%3D; cna=nLBAE/hjITYCAXJbylmgphSU; cpSTAT_ok_times=1; CNZZDATA1256416394=800638299-1522123216-https%253A%252F%252Fwww.damai.cn%252F%7C1522123216; cpSTAT_ok_pages=5; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%221626592db812d3-029871ed0ccafd-33697b04-384000-1626592db82362%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201522124133%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201522124133%7D%2C%22initial_view_time%22%3A%20%221522117816%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%7D; isg=BBkZOHCTpzGh6HulaeJafF3mKAMzDgyzXkZmETvMKcMuQj_Ug_eUKAe0QAc0eqWQ', 'Host': 'search.damai.cn', 'Origin': 'https://search.damai.cn', 'Referer': 'https://search.damai.cn/search.html?spm=a2o6e.home.0.0.591b48d3a1nUYO&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1', 'X-Requested-With': 'XMLHttpRequest'}
data = {'keyword': '', 'cty': '', 'ctl': '', 'currPage': str(fist_page), 'singleChar': '', 'tn': '', 'sctl': '', 'tsg': '0', 'order': '1'}


response = requests.post(url ='https://search.damai.cn/searchajax.html',headers=headers,data=data)
