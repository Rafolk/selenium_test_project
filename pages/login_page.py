from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class LoginPage(Base):
    url_login_page = 'https://www.saucedemo.com/'

    # Locators
    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    text_main_page = "//span[@class='title']"

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.text_main_page)))
    # но слово вряд ли может быть кликабельным. хотя как поосмотреть...

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Ввод имени пользователя.")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод пароля.")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажатие на кнопку Login.")

    # Methods
    def authorization(self):
        self.driver.get(self.url_login_page)
        self.get_current_url()
        self.input_user_name('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()
        self.get_assert_text(self.get_main_word(), 'Products')
