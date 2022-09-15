

from homepage import HomePage
from excel_lib_pom import read_locators
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class RegistrationPage(HomePage):
    def __init__(self,driver) :
        super().__init__(driver)

    locators = read_locators("registrationpage")

    def reg_click_gender(self):
        element = RegistrationPage.locators["rdo_male"]
        self.click_element(element)

    def reg_enter_fname(self, fname):
        element = RegistrationPage.locators["txt_fname"]
        self.enter_text(element , value=fname)

    def reg_enter_lname(self, lname):
        element = RegistrationPage.locators["txt_lname"]
        self.enter_text(element, value=lname)

    def reg_enter_email(self, email):
        element = RegistrationPage.locators["txt_email"]
        self.enter_text(element, value=email)

    def reg_enter_password(self, password):
        element = RegistrationPage.locators["txt_password"]
        self.enter_text(element, value=password)

    def reg_enter_confirm_password(self, confirm_password):
        element = RegistrationPage.locators["txt_confirm_password"]
        self.enter_text(element, value=confirm_password)

    def reg_click_register_btn(self):
        element = RegistrationPage.locators["btn_register"]
        self.click_element(element)
        
    def is_user_registration_Successful(self,message):
        _xpath = f"//div[contains(text(),'{message}')]"
        for _ in range(10):
            try:
                return self.driver.find_element("xpath",_xpath).is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False
    