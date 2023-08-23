from colorama import Fore

from src.audio import Audio
from src.config import Config
from src.web_scraper import WebScraper


class DownloadPodcast:

    def __init__(self, podcast_name, episode_name, latest_episode):
        self.podcast_name = podcast_name.lower()
        self.episode_search_name = episode_name
        self.latest_episode = latest_episode
        self.episode_name = None
        self.config = Config()
        self.podcast_url = self.get_podcast_url
        self.web_scraping = WebScraper()
        self.audio = Audio()

    @property
    def get_podcast_url(self):

        return self.config.get_podcast_url(self.podcast_name)

    def download_episode(self):
        self.web_scraping.start_connection(self.podcast_url)
        if self.latest_episode:
            episode_element_in_podcast_page = self.get_last_episode()
        else:
            episode_element_in_podcast_page = self.search_episode()
        self.web_scraping.click_element(episode_element_in_podcast_page)
        chapter_page = self.web_scraping.find_element_by_id('dlink')
        self.web_scraping.click_element(chapter_page)
        self._get_audio_url()
        self.web_scraping.close_connection()

    def get_last_episode(self):
        xpath_paths = [
            '//*[@id="main"]/div/div[4]/div/div/div[1]/div/div/div[1]/div[4]/p[1]/a',
           '//*[@id="main"]/div/div[3]/div/div/div[1]/div/div/div[1]/div[4]/p[1]/a'
        ]
        episode_element_in_podcast_page = None
        for xpath in xpath_paths:
            try:
                episode_element_in_podcast_page = self.web_scraping.find_element_by_xpath(xpath)
                break
            except Exception:
                print('XPath did not match, trying a different one')
        if episode_element_in_podcast_page is None:
            raise Exception('Could not find the last episode of the podcast: {}'.format(self.podcast_name))
        self._save_chapter_name(episode_element_in_podcast_page)

        return episode_element_in_podcast_page

    def search_episode(self):
        page_count = 0
        while True:
            print('Searching episode...')
            try:
                episode_element_in_podcast_page = self.web_scraping.find_element_by_partial_text(
                    self.episode_search_name
                )
            except:
                if page_count < 10:
                    print('Searching episode...')
                    page_count += 1
                    next_page = self.web_scraping.find_element_by_xpath(
                        '//*[@id="main"]/div/div[4]/div/nav/ul/li[12]/a'
                    )
                    self.web_scraping.click_element(next_page)
                else:
                    raise Exception('No found podcast with title: {}'.format(self.episode_search_name))
            else:
                break
        self._save_chapter_name(episode_element_in_podcast_page)

        return episode_element_in_podcast_page

    def _save_chapter_name(self, podcast_page):
        self.episode_name = podcast_page.get_attribute('title')
        print(Fore.GREEN, 'Podcast found! ', Fore.BLUE, self.episode_name)

    def _get_audio_url(self):
        episode_audio_page = self.web_scraping.driver.current_url
        self.audio.download_episode_audio(episode_audio_page, self.episode_name)
