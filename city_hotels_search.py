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
        time.sleep(10)
        driver.find_element_by_css_selector('#slimmenu > div:nth-child(3) > a > span.mobile-menu-text').click()
        time.sleep(5)
        button=driver.find_element_by_css_selector('#slimmenu > div:nth-child(3) > div.mega-menu-container.row > div > div:nth-child(3) > ul > li.border-0.mobile-none > a')
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(button).click(button).perform()
        time.sleep(3)

obj = RunTestClass()
obj.testMethod()