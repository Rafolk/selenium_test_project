from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CheckoutOverviewPage(Base):

    # Locators
    finish_button = "//button[@id='finish']"

    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.finish_button)))

    # Actions
    def click_finish_button(self):
        self.get_finish_button().click()
        print("Окончательное подтверждение заказа в корзине кнопкой Finish.")

    # Methods
    def finish_order(self):
        self.click_finish_button()
        self.get_current_url()
