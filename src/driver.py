import os
from sys import platform
import requests
import zipfile

from src.config import Config


class Driver():
    
    _LINUX = 'chromedriver_linux64.zip'
    _DARWIN = 'chromedriver_mac64.zip'
    _WIN32 = 'chromedriver_win32.zip'
    _CHROMEDRIVER_PATH = os.path.join(os.path.dirname(__file__).replace('src', 'chromedriver'))
    
    def __init__(self):
        self.config = Config()
        self.browser_version = self._get_chrome_version()
        self.driver_file = None
    
    def _extract_version(self, output):
        try:
            google_version = ''
            for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
                if letter != '\n':
                    google_version += letter
                else:
                    break
            return(google_version.strip())
        except TypeError:
            return

    def _get_chrome_version(self):
        version = None
        install_path = None

        try:
            if platform == "linux" or platform == "linux2":
                # linux
                install_path = "/usr/bin/google-chrome"
            elif platform == "darwin":
                # OS X
                install_path = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
            elif platform == "win32":
                # Windows
                stream = os.popen(
                        'reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows'
                        '\\CurrentVersion\\Uninstall\\Google Chrome"'
                    )
                output = stream.read()
                version = self._extract_version(output)
        except Exception as ex:
            print(ex)

        version = os.popen(f"{install_path} --version").read().strip('Google Chrome ').strip() if install_path else version

        return version
    
    def _download_driver(self):
        driver_url = self.config.get_driver('path')
        
        if platform == "linux" or platform == "linux2":
            so = self._LINUX
        elif platform == "darwin":
            so = self._DARWIN
        elif platform == "win32":
            so = self._WIN32
        else: raise
        
        download_url = driver_url.format(self.browser_version, so)
        self._create_driver_folder()
        self.driver_file = os.path.join(self._CHROMEDRIVER_PATH, 'chromedriver.zip')
        
        response = requests.get(download_url)
        open(self.driver_file, 'wb').write(response.content)
        
    def _create_driver_folder(self):
        if not os.path.exists(self._CHROMEDRIVER_PATH):
            os.mkdir(self._CHROMEDRIVER_PATH)
        
    def extract_file(self):
        with zipfile.ZipFile(self.driver_file, 'r') as zip_ref:
            zip_ref.extractall(self._CHROMEDRIVER_PATH)
        os.remove(self.driver_file)

    def get_driver(self):
        self._download_driver()
        self.extract_file()