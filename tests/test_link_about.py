from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_link_about():
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=o)

    login = LoginPage(driver)
    login.authorization()

    go_to_link_about = MainPage(driver)
    go_to_link_about.go_to_link_about()
