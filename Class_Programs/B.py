from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Firefox(GeckoDriverManager().install())
driver.get("https://www.google.com")