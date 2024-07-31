import time
from selenium.webdriver import Chrome

web = Chrome()
# web.get("https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=207846549&clazzid=15774749")
web.get("https://mooc2-ans.chaoxing.com/mooc2-ans/mycourse/stu?courseid=207846549&clazzid=15774749&cpi=76225853&enc=3430f669916bc93f78593875907a3006&t=1718955463617&pageHeader=1&v=2")

# login
phone = web.find_element("name", 'ipt-tel')
pwd = web.find_element("name", 'ipt-pwd')
login = web.find_element("name", 'btn-big-blue')

phone.send_keys('13540266394')
pwd.send_keys('Artist_78')
login.click()
time.sleep(2)