from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __int__(self, driver):
        self.driver = driver

    def authorization(self, driver, login_name, login_password):
        user_name = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH,
                                                                                   "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print("Введён логин.")

        password = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH,
                                                                                   "//input[@id='password']")))
        password.send_keys(login_password)
        print("Введён пароль.")

        button_login = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH,
                                                                                      "//input[@id='login-button']")))
        button_login.click()
        print("Вход по кнопке Login.")
