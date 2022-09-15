from selenium.webdriver.support.select import Select
from Wait import _wait

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @_wait      # click_element = _wait(click_element)
    def click_element(self, locator):
        self.driver.find_element(*locator).click()       # find_element("id", "fname")

    @_wait  # enter_text = _wait(enter_wait)
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @_wait  # select_item = _wait(select_item)
    def select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise Exception