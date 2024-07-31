# https://www.cnblogs.com/nonamelake/p/14509308.html
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# StaleElementReferenceException on Python Selenium
# https://stackoverflow.com/questions/27003423/staleelementreferenceexception-on-python-selenium
timeout = 25
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)

progress_pattern = re.compile("(\s)*任务(\s)*(?P<num>\d+)(\s)*(\S)+(?P<suffix>.[a-zA-Z0-9]+)(\s)*(\S)*(\s)*\n进度(\s)*(\S)*(\s)*(?P<progress>\d+%)")

# # keep window open
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

# open website
driver.get('https://yqdx.yunxuetang.cn/login.htm')
# switch to new tab window handle
driver.switch_to.window(driver.window_handles[-1])
print("line 29, driver.current_window_handle = ", driver.current_window_handle)

# login
time.sleep(2)  # wait 2 seconds
username = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((
    By.XPATH, "//input[@id='txtUserName2']")))
# username = driver.find_element(By.XPATH, "//input[@id='txtUserName2']")
password = driver.find_element(By.XPATH, "//input[@id='txtPassword2']")
check = driver.find_element(By.XPATH, "//input[@id='chkloginpass']")
login = driver.find_element(By.XPATH, "//input[@id='btnLogin2']")
username.send_keys('10241787')
password.send_keys('Wisps_3faw01')
check.click()

time.sleep(2)  # wait 2 seconds
login.click()
time.sleep(2)  # wait 2 seconds
# switch to new tab window handle
driver.switch_to.window(driver.window_handles[-1])
print("line 48, driver.current_window_handle = ", driver.current_window_handle)

# open "我的学习" Tab
time.sleep(2)  # wait 2 seconds`
myLearn = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((
    By.LINK_TEXT, "我的学习")))
# myLearn = driver.find_element(By.LINK_TEXT, "我的学习")
time.sleep(2)  # wait 2 seconds
myLearn.click()
# switch to new tab window handle
driver.switch_to.window(driver.window_handles[-1])
print("line 59, driver.current_window_handle = ", driver.current_window_handle)

# https://juejin.cn/posbtnt/7151739448680513543
# Debug: Chrome -> F12 -> Console ->
# $ ServiceWorkRegistration
# $ document.getElementByClassName('st')
# in CSS, Space means dot iterator (.)
# learns = driver.find_elements(By.CLASS_NAME, 'btn btn-text-info lh20 w-100')
# learns = driver.find_elements(By.CLASS_NAME, 'btn.btn-text-info.lh20.w-100')
# choose the last one
time.sleep(2)  # wait 5 seconds
one_task = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((
    By.CLASS_NAME, 'btn-text-info.lh20.w-100')))
try:
    time.sleep(2)  # wait 5 seconds
    tasks = driver.find_elements(By.CLASS_NAME, 'btn-text-info.lh20.w-100')
    print("line 75, tasks = ", tasks)
except Exception as e:
    # https://www.cnblogs.com/cnkemi/p/8985654.html
    file_name = "tasks_exception.png"
    driver.get_screenshot_as_file(file_name)
    print("####################")
    print("tasks exception: ", e)
    print("####################")
    time.sleep(2)  # wait 2 seconds
    # raise  # throw an exception

# for task in tasks:
for task_index in range(len(tasks)):
    print("line 88, task_index = ", task_index)
    try:
        # driver.back()
        driver.close()
        time.sleep(2)
        # switch to new tab window handle
        driver.switch_to.window(driver.window_handles[-1])
        print(driver.current_window_handle)
        driver.refresh()

        # time.sleep(2)  # wait 5 seconds
        # # window is already changed, tasks will be []
        # # switch to default window handle
        # driver.switch_to.window(driver.window_handles[0])
        print("line 106, driver.current_window_handle = ", driver.current_window_handle)
        tasks = driver.find_elements(By.CLASS_NAME, 'btn-text-info.lh20.w-100')
        print("line92, tasks = ", tasks)
    except Exception as e:
        # https://www.cnblogs.com/cnkemi/p/8985654.html
        file_name = "tasks_exception.png"
        driver.get_screenshot_as_file(file_name)
        print("####################")
        print("tasks exception: ", e)
        print("####################")
        time.sleep(2)  # wait 2 seconds
        # raise  # throw an exception

    tasks[task_index].click()
    time.sleep(2)  # wait 2 seconds
    # switch to new tab window handle
    driver.switch_to.window(driver.window_handles[-1])
    print("line 106, driver.current_window_handle = ", driver.current_window_handle)

    try:
        time.sleep(2)  # wait 5 seconds
        learns = driver.find_elements(By.XPATH, "//tr[@class='hand']")
        print("112, learns = ", learns)
    except Exception as e:
        # https://www.cnblogs.com/cnkemi/p/8985654.html
        file_name = "learns_exception.png"
        driver.get_screenshot_as_file(file_name)
        print("####################")
        print("tasks exception: ", e)
        print("####################")
        time.sleep(2)  # wait 2 seconds
        # raise  # throw an exception

    # for learn in learns:
    for learn_index in range(len(learns)):
        time.sleep(2)
        driver.refresh()
        try:
            time.sleep(2)  # wait 5 seconds
            learns = driver.find_elements(By.XPATH, "//tr[@class='hand']")
            print("line 130, learns = ", learns)
        except Exception as e:
            # https://www.cnblogs.com/cnkemi/p/8985654.html
            file_name = "learns_exception.png"
            driver.get_screenshot_as_file(file_name)
            print("####################")
            print("tasks exception: ", e)
            print("####################")
            time.sleep(2)  # wait 2 seconds
            # raise  # throw an exception
        # check if learn complete: 100% for complete, else not
        re_result = progress_pattern.search(learns[learn_index].text)
        # switch to new tab window handle
        driver.switch_to.window(driver.window_handles[-1])
        print("line 165, driver.current_window_handle = ", driver.current_window_handle)
        if re_result is None:
            continue
        elif re_result.group('progress') == '100%':  # complete and do not need learn
            continue
        else:
            time.sleep(2)  # wait 2 seconds
            learns[learn_index].click()
            time.sleep(2)  # wait 2 seconds
            # switch to new tab window handle
            driver.switch_to.window(driver.window_handles[-1])
            print("line 154, driver.current_window_handle = ", driver.current_window_handle)

            # may display "您正在学习另一个知识 xxx ，请将知识 xxx 学习页关闭后再次进入该知识学习"
            try:
                # resumeLearn = driver.find_element(By.XPATH, "//input[@class='btnok']")
                resumeLearn = driver.find_element(By.LINK_TEXT, "继续学习")
                resumeLearn.click()
            except Exception as e:
                # https://www.cnblogs.com/cnkemi/p/8985654.html
                file_name = "learns_exception.png"
                driver.get_screenshot_as_file(file_name)
                print("####################")
                print("resumeLearn exception: ", e)
                print("没有继续学习弹窗页面", e)
                print("####################")
                time.sleep(2)  # wait 2 seconds

            while True:
                try:
                    status = driver.find_element(By.XPATH, "//span[@id='ScheduleText']")
                except Exception as e:
                    # https://www.cnblogs.com/cnkemi/p/8985654.html
                    file_name = "learns_exception.png"
                    driver.get_screenshot_as_file(file_name)
                    print("####################")
                    print("status exception: ", e)
                    print("####################")
                    time.sleep(2)  # wait 2 seconds
                    raise

                if status.text is None:
                    break
                elif status.text == '100%': # complete and close
                    # driver.back()
                    driver.close()
                    time.sleep(2)
                    # switch to new tab window handle
                    driver.switch_to.window(driver.window_handles[-1])
                    print(driver.current_window_handle)
                    driver.refresh()
                    break
                else:
                    time.sleep(10)