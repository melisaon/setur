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
        driver.find_element_by_css_selector('#CheckinDate').click()
        driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-top > div.datepicker-days > table > tbody > tr:nth-child(6) > td:nth-child(5)').click()
        driver.find_element_by_css_selector('#CheckoutDate')
        driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-top > div.datepicker-days > table > tbody > tr:nth-child(1) > td:nth-child(5)').click()
        driver.find_element_by_css_selector('#hotel-search-1 > div > div:nth-child(5) > a').click()
        button=driver.find_element_by_css_selector('#flight-search-1 > div.row.justify-end > div.custom-btn.mfp-close1')
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(button).click(button).perform()
        time.sleep(3)

obj = RunTestClass()
obj.testMethod()



