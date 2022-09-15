from webdriver_manager.chrome import ChromeDriverManager

class Config:
    DRIVER_PATH = ChromeDriverManager().install()
    URL = "http://demowebshop.tricentis.com/"
    MAX_TIMEOUT = 20