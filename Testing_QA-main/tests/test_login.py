import time

from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_chrome(driver):
    driver.get("https://my.proweb.uz/log-in")
    login_page = LoginPage(driver)
    login_page.enter_phone_number("998337019484")
    login_page.click_btn_next()

    login_page.enter_password("Ychiha14078828+")
    login_page.click_btn_submit()
    login_page.click_btn_sessions()
    login_page.click_btn_finish()


    try:
        login_page.click_btn_sessions()
        login_page.click_btn_finish()
    except:
        pass


    home_page = HomePage(driver)
    home_page.click_profile_icon()
    time.sleep(5)
    home_page.click_exit_btn()
    home_page.click_confirm_exit()





