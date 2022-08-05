import os
import requests
from colorama import Fore


class Audio():

    _DOWNLOADED_AUDIO_PATH = os.path.join(os.path.dirname(__file__).replace('src', 'downloaded_podcast_audio'))
    
    def download_audio(self, audio_url, chapter_name):
        doc = requests.get(audio_url)
        
        try:
            if not os.path.exists(self._DOWNLOADED_AUDIO_PATH):
                os.mkdir(self._DOWNLOADED_AUDIO_PATH)
            download_name = '{}.mp3'.format(chapter_name)
            
            with open(os.path.join(self._DOWNLOADED_AUDIO_PATH, download_name), 'wb') as f:
                f.write(doc.content)
            print(
                    Fore.GREEN + 'Podcast downloaded! ' 
                    + Fore.BLUE + chapter_name 
                    + Fore.RESET + ' checkout in: ' + self._DOWNLOADED_AUDIO_PATH
                )
        except:
            raise Exception('Error saving podcast chapter')