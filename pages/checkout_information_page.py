from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from faker import Faker


class CheckoutInformationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name_field = "//input[@id='first-name']"
    last_name_field = "//input[@id='last-name']"
    postal_code_field = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    # Getters
    def get_first_name_field(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_postal_code_field(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.postal_code_field)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name_field().send_keys(first_name)
        print("Ввод имени.")

    def input_last_name(self, last_name):
        self.get_last_name_field().send_keys(last_name)
        print("Ввод фамилии.")

    def input_postal_code(self, postal_code):
        self.get_postal_code_field().send_keys(postal_code)
        print("Ввод почтового индекса.")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Подтверждение информации кнопкой Continue.")

    # Methods
    def input_and_confirm_checkout_information(self):
        fake = Faker("ru_RU")
        self.input_first_name(fake.first_name())
        self.input_last_name(fake.last_name())
        self.input_postal_code(fake.postcode())
        self.click_continue_button()
        self.get_current_url()
