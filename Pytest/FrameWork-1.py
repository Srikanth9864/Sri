from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

driver = Chrome("/Users/sandeep/Desktop/Training/_selenium/chromedriver")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(3)
# 1. Check if the element is loaded in the DOM
# 2. Check if the element is visible on the webpage.
# 3. Check if the element is enabled or not?

class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)   # initlising parent class constructor

    # over-riding __call__ method of parent class
    def __call__(self, driver):
        print("Calling __call__ method of Child Class")
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            # Extra functionality that you are adding in child class
            # checking for enablement of the element
            return result.is_enabled()
        else:
            return False

# w = WebDriverWait(driver, 20)
# v = _visibility_of_element_located(("xpath", "//div[text()='100%']"))
# w.until(v, message="Progress bar was not loaded even after 20 seconds")
# print("DONE!")

def _wait(func):
    def wrapper(*args, **kwargs):
        # 1. Check if the element is loaded in the DOM
        # 2. Check if the element is visible on the webpage.
        # 3. Check if the element is enabled or not?
        locator = args[0]       # args = (("link text", "Register"),)
        w = WebDriverWait(driver, 20)
        v = _visibility_of_element_located(locator)
        w.until(v, message="Progress bar was not loaded even after 20 seconds")
        # Original func gets executed (click_element, enter_text, select_item)
        return func(*args, **kwargs)
    return wrapper

@_wait      # click_element = _wait(click_element)
def click_element(locator):
    driver.find_element(*locator).click()       # find_element("id", "fname")

@_wait  # enter_text = _wait(enter_wait)
def enter_text(locator, *, value):
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)

@_wait  # select_item = _wait(select_item)
def select_item(locator, *, item):
    element = driver.find_element(*locator)
    s = Select(element)
    if isinstance(item, str):
        s.select_by_visible_text(item)
    elif isinstance(item, int):
        s.select_by_index(item)
    else:
        raise Exception

click_element((By.LINK_TEXT, "Register"))
click_element((By.ID, "gender-male"))
enter_text((By.NAME, "FirstName"), value="hello")
enter_text((By.XPATH, "//input[@name='LastName']"), value="world")
enter_text((By.CSS_SELECTOR, "input[name='Email']"), value="hello.world@company.com")
enter_text((By.ID, "Password"), value="Password123")
enter_text((By.ID, "ConfirmPassword"), value="Password123")
click_element((By.ID, "register-button"))
driver.close()