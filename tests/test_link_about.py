from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_link_about(driver):
    login = LoginPage(driver)
    login.authorization()

    go_to_link_about = MainPage(driver)
    go_to_link_about.go_to_link_about()
