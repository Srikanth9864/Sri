from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from Config import Config

class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)   # initlising parent class constructor

    # over-riding __call__ method of parent class
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            # Extra functionality that you are adding in child class
            # checking for enablement of the element
            return result.is_enabled()
        else:
            return False

def _wait(func):
    def wrapper(*args, **kwargs):
        # 1. Check if the element is loaded in the DOM
        # 2. Check if the element is visible on the webpage.
        # 3. Check if the element is enabled or not?
        instance = args[0]      # args = (self, ("link text", "Register"))
        locator = args[1]       
        w = WebDriverWait(instance.driver, Config.MAX_TIMEOUT)
        v = _visibility_of_element_located(locator)
        w.until(v, message="Progress bar was not loaded even after 20 seconds")
        # Original func gets executed (click_element, enter_text, select_item)
        return func(*args, **kwargs)
    return wrapper