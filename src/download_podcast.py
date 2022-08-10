from colorama import Fore

from src.web_scraper import WebScraper
from src.audio import Audio
from src.config import Config


class DownloadPodcast():
    
    def __init__(self, podcast_name, chapter_search_name):
        self.podcast_name = podcast_name.lower()
        self.chapter_search_name = chapter_search_name
        self.chapter_name = None
        self.config = Config()
        self.podcast_url = self.get_podcast_url
        self.web_scraping = WebScraper()
        self.audio = Audio()
        
    @property
    def get_podcast_url(self):

        return self.config.get_podcast_url(self.podcast_name)
            
    def download_podcast(self):
        self.web_scraping.start_connection(self.podcast_url)
        podcast_page = self.search_podcast()
        self.web_scraping.click_element(podcast_page)
        chapter_page = self.web_scraping.find_element_by_id('dlink')
        self.web_scraping.click_element(chapter_page)
        self._get_audio_url()
        self.web_scraping.close_connection()
        
    def search_podcast(self):
        page_count = 0
        while True:
            print('Searching podcast...')
            try:
                element = self.web_scraping.find_element_by_partial_text(self.chapter_search_name)
            except:
                if page_count < 10:
                    print('Searching podcast...')
                    page_count += 1
                    next = self.web_scraping.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/nav/ul/li[12]/a')
                    self.web_scraping.click_element(next)
                else:
                    raise Exception('No found podcast with title: {}'.format(self.chapter_search_name))
            else:
                break
        self._save_chapter_name(element)
        print(Fore.GREEN, 'Podcast found! ', Fore.BLUE, self.chapter_name)

        return element
    
    def _save_chapter_name(self, podcast_page):
        self.chapter_name = self.chapter_name = podcast_page.get_attribute('title')
            
    def _get_audio_url(self):
        audio_url = self.web_scraping.driver.current_url
        self.audio.download_audio(audio_url, self.chapter_name)
