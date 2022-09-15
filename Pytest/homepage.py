from selenium.common.exceptions import NoSuchElementException
from excel_lib_pom import read_locators
from Selenium_wrapper import SeleniumWrapper
from time import sleep

class HomePage(SeleniumWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        
    locators = read_locators("homepage")

    def homepage_click_login(self):
        element = HomePage.locators['lnk_login']
        self.click_element(element)
    
    def homepage_click_register(self):
        element = HomePage.locators['lnk_register']
        self.click_element(element)
    
    def is_user_logged_in(self, email):
        _xpath = f"//a[text()='{email}']"
        for _ in range(5):
            try:
                return self.driver.find_element("xpath", _xpath).is_displayed()
            except NoSuchElementException:
                print("User is not logged in yet.. trying after one second")
                sleep(1)
                continue
        return False

    
    


 