from homepage import HomePage
from registrationpage import RegistrationPage
from time import sleep

def test_registration(setup):
    hp = HomePage(setup)
    hp.homepage_click_register()
    rp = RegistrationPage(setup)
    rp.reg_click_gender()
    rp.reg_enter_fname("Srik")
    rp.reg_enter_lname("anth")
    rp.reg_enter_email("hell3s@gmail.com")
    rp.reg_enter_password("password123")
    rp.reg_enter_confirm_password("password123")
    rp.reg_click_register_btn()
    assert rp.is_user_registration_Successful("Your registration completed")==True
    

