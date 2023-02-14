import os

import requests
from colorama import Fore


class Audio:

    _DOWNLOADED_AUDIO_PATH = os.path.join(os.path.dirname(__file__).replace('src', 'downloaded_podcast_audio'))
    
    def download_episode_audio(self, episode_audio_page, episode_name):
        episode_audio = requests.get(episode_audio_page)
        
        try:
            if not os.path.exists(self._DOWNLOADED_AUDIO_PATH):
                os.mkdir(self._DOWNLOADED_AUDIO_PATH)
            download_episode_audio_name = '{}.mp3'.format(episode_name)
            
            with open(os.path.join(self._DOWNLOADED_AUDIO_PATH, download_episode_audio_name), 'wb') as f:
                f.write(episode_audio.content)
            print(
                Fore.GREEN + 'Podcast downloaded! '
                + Fore.BLUE + episode_name
                + Fore.RESET + ' checkout in: ' + self._DOWNLOADED_AUDIO_PATH
                )
        except:
            raise Exception('Error saving podcast chapter')
