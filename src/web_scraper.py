from genericpath import isfile
import os

from click import option
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from src.config import Config
from src.driver import Driver


class WebScraper():
    
    def __init__(self, headless=True, muted=True):
        self.config = Config()
        self.driver_tools = Driver()
        self.headless = headless
        self.muted = muted
        self.options = self._set_webdriver_options
        self.driver = self._chromedriver_driver

    @property
    def _set_webdriver_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        if self.headless:
            options.add_argument("--headless")
        if self.muted:
            options.add_argument("--mute-audio")
        
        return options

    @property
    def _chromedriver_driver(self):
        
        try:
            return webdriver.Chrome(self._driver_path(), chrome_options=self.options)
        except:
            self.driver_tools.get_driver()
            return webdriver.Chrome(self._driver_path(), chrome_options=self.options)

    def _driver_path(self):
        driver_path = os.path.join(os.path.dirname(__file__).replace('src', 'chromedriver'), 'chromedriver')
        
        if os.path.isfile(driver_path):
            return driver_path
        else:
            raise Exception('Chromedriver missing!')
 
    def start_connection(self, url):
        self.driver.get(url)

    def click_element(self, element):
        try:
            element = self.driver.execute_script("arguments[0].click();", element)
        except WebDriverException:
            print('Element is not clickable')
     
    def find_element_by_partial_text(self, chapter_search_name):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, chapter_search_name)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_element_by_id(self, id):
        return self.driver.find_element(By.ID, id)
    
    def close_connection(self):
        self.driver.quit()