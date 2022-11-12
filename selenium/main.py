from selenium import webdriver
from webdriver_manager.firefox import FirefoxDriverManager

from webdriver_manager.core.utils import read_version_from_cmd, PATTERN
version = read_version_from_cmd("/usr/bin/firefox-bin --version", PATTERN["firefox"])
driver_binary = FirefoxDriverManager(version=version).install()
