import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from src.config import Config


class WebScraper:

    def __init__(self, headless=True, muted=True):
        self.config = Config()
        self.headless = headless
        self.muted = muted
        self.options = self._set_webdriver_options

        service = Service()
        self.driver = webdriver.Chrome(service=service, options=self.options)

    @property
    def _set_webdriver_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        if self.headless:
            options.add_argument("--headless")
        if self.muted:
            options.add_argument("--mute-audio")
        return options

    def start_connection(self, url):
        self.driver.get(url)

    def click_element(self, element):
        try:
            self.driver.execute_script("arguments[0].click();", element)
        except WebDriverException:
            print('Element is not clickable')

    def find_element_by_partial_text(self, chapter_search_name):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, chapter_search_name)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def find_element_by_id(self, html_id):
        return self.driver.find_element(By.ID, html_id)

    def close_connection(self):
        self.driver.quit()
