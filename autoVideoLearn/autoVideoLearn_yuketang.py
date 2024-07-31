# https://www.cnblogs.com/nonamelake/p/14509308.html
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import pyperclip

driver = webdriver.Firefox()

# 打开网页
driver.get('https://www.luffycity.com/')
# 登录
# 窗口最大化
driver.maximize_window()
# 先关闭广告弹窗，<img src="//hcdn2.luffycity.com/media/frontend/activity/close.png" class="close" data-v-250c3340="">
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/img[1]').click()
# 然后点击登录按钮
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/header/div/div/div[2]/div[2]/span')))
driver.find_element_by_xpath('/html/body/div[1]/div/div/header/div/div/div[2]/div[2]/span').click()
# 输入用户名，密码
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/input').send_keys('username')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/input').clear()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/input').send_keys(
    'password')
# 点击登录
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/button').click()
sleep(3)
# 打开一个课程链接
driver.get('https://www.luffycity.com/play/13735')

# 循环下面的步骤
def record_screen(count):
    for i in range(count):
        # 点击一次刷新按钮
        driver.refresh()
        # 当全屏按钮出现时,点击全屏按钮,<button type="button" class="pv-fullscreen pv-iconfont pv-icon-fullscreen"></button>
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div[8]/button')))
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div[8]/button').click()
        # 点击开始
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div[4]/span').click()
        # 使用autogui，通过快捷键ctrl+F1开始录屏
        pyautogui.hotkey('ctrl', 'F1')
        # 等待5s,查询class="section active"下面的h5的名称,并copy，<h5 data-v-559c3ed2="" class="section-number">1.313 第89天：Flask初始化配置</h5>
        sleep(5)
        video_name = driver.find_element_by_xpath("//div[@class='section active']/section/h5").get_attribute(
            'textContent')
        video_name_postfix = video_name + '.wmv'
        pyperclip.copy(video_name_postfix)
        # 每过10s检查一次pv-time-current时间,如果pv-time-current时间=pv-time-duration,通过快捷键ctrl+F2结束录屏,并退出while循环
        # <span class="pv-time-current">00:21</span>，<span class="pv-time-duration">38:44</span>
        while True:
            pv_time_current = driver.find_element_by_class_name("pv-time-current").get_attribute('textContent')
            pv_time_duration = driver.find_element_by_class_name("pv-time-duration").get_attribute('textContent')
            if pv_time_current == pv_time_duration:
                print('视频播放完成：', video_name_postfix)
                pyautogui.hotkey('ctrl', 'F2')
                break
            else:
                sleep(10)
        # paste上面copy的名称+wmv后缀,用autogui切换到浏览器,按ESC退出全屏
        sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('alt', 'tab')
        sleep(1)
        pyautogui.hotkey('esc')
        sleep(1)
        # 检查是否有反馈弹窗，如果有就点击关闭按钮，<img data-v-225eb798="" src="//hcdn2.luffycity.com/media/frontend/activity/icon-close.png" alt="关闭按钮">
        pop_window_feedback = '/html/body/div[1]/div/div/div/div[1]/div[3]/div/p[1]/img'
        pop_window_next = '/html/body/div[1]/div/div/div/div[1]/div[3]/button'
        try:
            # driver.find_element_by_xpath(pop_window_feedback)
            driver.find_element_by_xpath(pop_window_feedback).click()
            driver.find_element_by_xpath(pop_window_next).click()
        except:
            # 如果没有反馈弹窗，就点击下一节按钮，<button data-v-559c3ed2="" class="next-button">下一节</button>
            driver.find_element_by_xpath(pop_window_next).click()

        print(i)

record_screen(200)
