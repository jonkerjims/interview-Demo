import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestLogin:
    def __init__(self):
        self.username = '20723055'
        self.passwd = '020013'

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\JasonXue\file\spyder\chromedriver_win32\chromedriver')
        self.driver.maximize_window()
        self.url = 'http://fresh.ahau.edu.cn/yxxt-v5/web/xsLogin/login.zf;jsessionid=1336C8FE98E6CB7C4B397A8BD1EFE679?rdt=web%2Fjkxxtb%2FtbJkxx'
        self.driver.get(self.url)

    def test_login(self):
        self.driver.find_element_by_id('zh').clear()
        self.driver.find_element_by_id('zh').send_keys(self.username)
        self.driver.find_element_by_id('mm').clear()
        self.driver.find_element_by_id('mm').send_keys(self.passwd)
        self.driver.find_element_by_id('dlan').click()

    def self_html(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.alert.accept()
        self.driver.execute_script("document.getElementById('dqszdmc').removeAttribute('readOnly')")
        self.driver.find_element_by_id('dqszdmc').send_keys('安徽省合肥市蜀山区')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="jftbForm"]/div[17]/div/button').click()


robot = TestLogin()
robot.setUp()
time.sleep(3)
robot.test_login()
time.sleep(3)
robot.self_html()


