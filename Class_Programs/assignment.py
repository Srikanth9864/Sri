
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

# driver = Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(5)
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element("xpath","//button[contains(text(),'Click for JS Alert')]").click()
# driver.switch_to.alert.accept()

from time import sleep

driver = Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.srisrinivasabus.com/")
driver.find_element("xpath","//input[@id='search-onward-date']").click()
sleep(2)
driver.find_element("xpath","(//th[@class = 'next'])[1]").click()
sleep(2)
driver.find_element("xpath","(//th[@class = 'prev'])[1]").click()
sleep(2)
driver.find_element("xpath","//td[@class and text()='18']").click()
