
from excel_lib_pom import read_locators
from homepage import HomePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class LoginPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    locators = read_locators("loginpage")
    def login_enter_email(self, email):
        element = LoginPage.locators['txt_email']
        self.enter_text(element, value=email)
    
    def login_enter_password(self, password):
        element = LoginPage.locators['txt_password']
        self.enter_text(element, value=password)

    def login_click_login(self):
        element = LoginPage.locators['btn_login']
        self.click_element(element)

    def _error_mesage(self,error_message):
            _xpath = f"//span[text()='{error_message}']"
            for _ in range(5):
                try:
                    return self.driver.find_element("xpath",_xpath).is_displayed()
                except NoSuchElementException:
                    print("Error Message not displayed")
                    sleep(1)
                    continue
            return False


# class LoginPage(SeleniumWrapper):
#     def __init__(self, driver):
#         super().__init__(driver)
    
#     _txt_email = ("id","Email")
#     _txt_password = ("id", "Password")
#     _btn_login = ("xpath", "//input[@value='Log in']")

#     def enter_email(self, email):
#         self.enter_text(LoginPage.txt_email, value=email)
    
#     def enter_password(self, password):
#         self.enter_text(LoginPage.txt_password, value=password)

#     def click_login(self):
#         self.click_element(LoginPage.btn_login)


