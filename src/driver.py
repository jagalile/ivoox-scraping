import os
import stat
import xml.etree.ElementTree as elemTree
import zipfile
from sys import platform

import requests
from requests.exceptions import InvalidURL

from src.config import Config


class Driver:

    _SO_VERSIONS = {
        'linux': 'chromedriver_linux64.zip',
        'linux2': 'chromedriver_linux64.zip',
        'darwin': 'chromedriver_mac64.zip',
        'win32': 'chromedriver_win32.zip',
    }
    _CHROMEDRIVER_PATH = os.path.join(os.path.dirname(__file__).replace('src', 'chromedriver'))
    _CHROMEDRIVER_VERSIONS_URL = 'https://chromedriver.storage.googleapis.com'
    
    def __init__(self):
        self.config = Config()
        self.browser_version = self._get_chrome_version
        self.driver_file = None

    @staticmethod
    def _extract_version(output):
        try:
            google_version = ''
            for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
                if letter != '\n':
                    google_version += letter
                else:
                    break
            return google_version.strip()
        except TypeError:
            return

    @property
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

        version = os.popen(f"{install_path} --version").read().strip('Google Chrome ').strip() \
            if install_path else version

        return version

    @staticmethod
    def _pre_format_chrome_version(version):
        version = version.rsplit('.', 1)[0]
        parsed_version = "{}.matched_version".format(version)
        return parsed_version
    
    def _download_driver(self):
        driver_url = self.config.get_driver('path')

        download_driver_url = driver_url.format(self._get_existing_chromedriver_version(), self._SO_VERSIONS[platform])
        
        try:
            self._create_driver_folder()
            self.driver_file = os.path.join(self._CHROMEDRIVER_PATH, 'chromedriver.zip')
            
            response = requests.get(download_driver_url)
            open(self.driver_file, 'wb').write(response.content)
        except InvalidURL:
            print('Invalid chromedriver url {}'.format(
                driver_url.format(self.browser_version, self._SO_VERSIONS[platform])
            ))
        
    def _create_driver_folder(self):
        if not os.path.exists(self._CHROMEDRIVER_PATH):
            os.mkdir(self._CHROMEDRIVER_PATH)
        
    def _extract_downloaded_driver_file(self):
        if self.driver_file is None:
            print('Driver file not found')
            raise
        with zipfile.ZipFile(self.driver_file, 'r') as zip_ref:
            zip_ref.extractall(self._CHROMEDRIVER_PATH)
        os.remove(self.driver_file)
        self._set_up_driver_file_permissions()

    def _get_existing_chromedriver_version(self):
        response = requests.get(self._CHROMEDRIVER_VERSIONS_URL)
        root = elemTree.fromstring(response.content)
        for k in root.iter('{http://doc.s3.amazonaws.com/2006-03-01}Key'):
            if self.browser_version.split('.')[0] in k.text.split('.')[0]:
                return k.text.split('/')[0]

    def _set_up_driver_file_permissions(self):
        for file in os.listdir(self._CHROMEDRIVER_PATH):
            os.chmod(os.path.join(self._CHROMEDRIVER_PATH, file), stat.S_IEXEC)

    def get_driver(self):
        self._download_driver()
        self._extract_downloaded_driver_file()
