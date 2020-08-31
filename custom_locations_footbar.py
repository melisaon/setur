from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import setur_test_automation_hotel_concept.config
import time

baseUrl = 'https://setur.com.tr'
locationChromeDriver = '../web_drivers/chromedriver'

class RunTestClass:
    def testMethod(self):
        driver = webdriver.Chrome(executable_path=locationChromeDriver)
        driver.get(baseUrl)
        time.sleep(5)
        driver.find_element_by_css_selector('#main-footer > div.container-fluid.p-0 > div.container-fluid.footer-end > div.container.bottom__end.flex.hidden-xs > div:nth-child(1) > ul > li:nth-child(5) > a').click()
        time.sleep(3)

obj = RunTestClass()
obj.testMethod()

