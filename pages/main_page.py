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
    add_to_cart_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    add_to_cart_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    burger_menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    # Getters
    def get_add_to_cart_product_1(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_product_1)))

    def get_add_to_cart_product_2(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_product_2)))

    def get_add_to_cart_product_3(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.link_about)))

    # Actions
    def click_add_to_cart_product_1(self):
        self.get_add_to_cart_product_1().click()
        print("Добавление в корзину товара 'Sauce Labs Backpack' (первый товар).")

    def click_add_to_cart_product_2(self):
        self.get_add_to_cart_product_2().click()
        print("Добавление в корзину товара 'Sauce Labs Bike Light' (второй товар).")

    def click_add_to_cart_product_3(self):
        self.get_add_to_cart_product_3().click()
        print("Добавление в корзину товара 'Sauce Labs Bolt T-Shirt' (третий товар).")

    def go_to_cart(self):
        self.get_cart().click()
        print("Переход в корзину.")

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print("Открытие бокового меню.")

    def click_link_about(self):
        self.get_link_about().click()
        print("Переход на ссылку About.")

    # Methods
    def methods_add_to_cart_product_1(self):
        self.click_add_to_cart_product_1()
        self.go_to_cart()
        self.get_current_url()

    def methods_add_to_cart_product_2(self):
        self.click_add_to_cart_product_2()
        self.go_to_cart()
        self.get_current_url()

    def methods_add_to_cart_product_3(self):
        self.click_add_to_cart_product_3()
        self.go_to_cart()
        self.get_current_url()

    def go_to_link_about(self):
        self.click_burger_menu()
        self.click_link_about()
        self.get_current_url()
        self.get_assert_current_url('https://saucelabs.com/')
