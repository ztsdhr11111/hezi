# Author : ZhangTong

import time

from config import *

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver import ActionChains 

class Hezi(object):
    def __init__(self):
        self.url = 'http://hezidev.hongru.com.cn/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

    def request(self, url):
        self.browser.get(url)

    def get_login_btn(self):
        login_btn = self.browser.find_element_by_xpath('//span[@id="status"]/a[2]')
        return login_btn

    def get_user_text(self):
        user_text = self.browser.find_element_by_id('account')
        return user_text

    def get_pwd_text(self):
        pwd_text = self.browser.find_element_by_id('password')
        return pwd_text

    def get_code_text(self):
        code_text = self.browser.find_element_by_id('code')
        return code_text

    def get_btn(self):
        btn = self.browser.find_element_by_id('btn_loginByPw')
        return btn

    def login_web(self):
        login_btn = self.get_login_btn()
        login_btn.click()
        time.sleep(2)
        user_text = self.get_user_text()
        user_text.send_keys(user_name)
        pwd_text = self.get_pwd_text()
        pwd_text.send_keys(password)

        input_code = self.get_code_text()
        code = input('请输入验证码')
        input_code.send_keys(code)
        btn = self.get_btn()
        btn.click()
        time.sleep(2)

    def get_quche_test(self):
        quche = self.browser.find_element_by_id('quche')
        return quche

    def get_county(self):
        county = self.browser.find_element_by_xpath('//div[@class="world"]/a[@title="Canada"]')
        return county

    def get_city(self):
        city = self.browser.find_element_by_xpath('//a[@title="Edmonton"]')
        return city

    def get_position(self):
        position = self.browser.find_element_by_xpath('//dl[@class="fixed"][1]/dd/a')
        return position

    def get_search_btn(self):
        search = self.browser.find_element_by_xpath('//a[@class="search-btn"]')
        return search

    def get_car(self):
        car = self.browser.find_element_by_xpath('//div[contains(@class,"list-all-model")][1]')
        return car.click()

    def more(self):
        more_btn = self.browser.find_element_by_xpath('//a[@class="more"][1]')
        return more_btn

    def get_order_btn(self):
        order_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "btn-reservation"')))
        return order_btn

    def switch_second_window(self):
        second = self.browser.window_handles[1]
        self.browser.switch_to_window(second)

    def choose_city(self):
        county = self.get_county()
        county.click()
        time.sleep(2)
        city = self.get_city()
        city.click()
        time.sleep(2)
        position = self.get_position()
        position.click()
        search = self.get_search_btn()
        search.click()
        time.sleep(10)

    def choose_car(self):
        car = self.get_car()
        car.click()
        more_btn = self.more()
        more_btn.click()
        self.switch_second_window()

    def run(self):
        self.browser.maximize_window()
        self.request(self.url)
        self.login_web()
        self.request(self.url)
        quche_btn = self.get_quche_test()
        quche_btn.click()
        time.sleep(2)
        self.choose_city()
        self.choose_car()
        order_btn = self.get_order_btn()
        order_btn.click()
        time.sleep(3)


if __name__ == '__main__':
    bro = Hezi()
    bro.run()
