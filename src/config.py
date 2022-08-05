import os
import configparser


class Config():
    
    _CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__).replace('src', ''), 'config.ini')
    
    def _load_config_file(self):
        config = configparser.ConfigParser()
        config.read(self._CONFIG_FILE_PATH)
        config.sections()
        
        return config
        
    def get_podcast_url(self, key):
        config = self._load_config_file()
        
        try:
            return config['PODCAST_URL'][key]
        except NameError:
            print('There is no podcast named {}'.format(key))
            raise
        
    def get_path(self, key):
        config = self._load_config_file()
        
        try:
            return config['PATHS'][key]
        except NameError:
            ('There is no path named {}'.format(key))
            raise