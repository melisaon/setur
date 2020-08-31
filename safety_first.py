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
        driver.find_element_by_css_selector('#CityRegion').send_keys(setur_test_automation_hotel_concept.config.hotelName)
        driver.find_element_by_css_selector('body > div.global-wrap > div.container.main-component.order-1.js-hotel > div.row.hotel-box.m-0 > div.col-md-4.col-12.hotel-box__small > div:nth-child(1) > div > div.place-link > a').click()
        driver.find_element_by_css_selector('#customsearch').send_keys(setur_test_automation_hotel_concept.config.hotelName)
        time.sleep(5)

obj = RunTestClass()
obj.testMethod()