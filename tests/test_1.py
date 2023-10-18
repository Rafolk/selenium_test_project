from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestSelectProduct:

    def test_select_product(self):
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)

        print("Начало теста.")

        login_standard_user = 'standard_user'
        password_all = 'secret_sauce'

        login = LoginPage()
        login.authorization(driver, login_standard_user, password_all)

        select_product = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, "//button["
                                                                                             "@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Добавили товар в корзину.")

        # Переход в корзину
        shopping_cart = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH,
                                                                                  "//a[@class='shopping_cart_link']")))
        shopping_cart.click()
        print("7_Перешли в корзину.")
