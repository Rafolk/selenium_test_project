from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_to_cart_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"

    # Getters
    def get_add_to_cart_product_1(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions
    def click_add_to_cart_product_1(self):
        self.get_add_to_cart_product_1().click()
        print("Добавление в корзину товара 'Sauce Labs Backpack' (первый товар).")

    def go_to_cart(self):
        self.get_cart().click()
        print("Переход в корзину.")

    # Methods
    def add_to_cart_product(self):
        self.click_add_to_cart_product_1()
        self.go_to_cart()
        self.get_current_url()
