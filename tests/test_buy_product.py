from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_buy_product_1():
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=o)

    login = LoginPage(driver)
    login.authorization()

    add_and_go_to_cart = MainPage(driver)
    add_and_go_to_cart.add_to_cart_product()
