from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(executable_path='/home/appuser/.wdm/drivers/geckodriver/linux64/0.32/geckodriver', options=options)
driver.get("https://google.com")
