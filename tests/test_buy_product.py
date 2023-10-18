from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_buy_product():
    o = Options()
    o.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=o)

    login = LoginPage(driver)
    login.authorization()

    # Переход в корзину
    shopping_cart = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH,
                                                                               "//a[@class='shopping_cart_link']")))
    shopping_cart.click()
    print("Перешли в корзину.")
