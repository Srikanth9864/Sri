
from registrationpage import RegistrationPage
from loginpage import LoginPage
from homepage import HomePage
from pytest import mark
from excel_lib_pom import read_headers,read_data
from time import sleep

headers = read_headers("smoke",'test_login_positive')
data = read_data("smoke",'test_login_positive')

@mark.parametrize(headers,data)
def test_login_positive(setup,email,password):
    hp = HomePage(setup)
    hp.homepage_click_login()
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()
    assert lp.is_user_logged_in(email)==True

headers = read_headers("smoke",'test_login_negative')
data = read_data("smoke",'test_login_negative')

@mark.parametrize(headers,data)
def test_login_negative(setup,email,password,error_message):
    hp = HomePage(setup)
    hp.homepage_click_login()
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()
    sleep(3)
    assert lp._error_mesage(error_message)==True
    
   