import os

import configparser


class Config:

    _CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__).replace('src', ''), 'config.ini')
    
    def _load_config_file(self):
        config = configparser.ConfigParser()
        config.read(self._CONFIG_FILE_PATH)
        config.sections()
        
        return config
    
    def _get_section_key_value(self, section, key):
        config = self._load_config_file()
        try:
            return config[section][key]
        except NameError:
            ('There is no path named {}'.format(key))
            raise
        
    def get_podcast_url(self, key):
        return self._get_section_key_value('PODCAST_URL', key)
        
    def get_path(self, key):
        return self._get_section_key_value('PATHS', key)
        
    def get_driver(self, key):
        return self._get_section_key_value('CHROME_DRIVER', key)
