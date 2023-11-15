from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class BackProductsPage(Base):

    # Locators
    back_to_products_button = "//button[@id='back-to-products']"

    # Getters
    def get_back_to_products_button(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.back_to_products_button)))

    # Actions
    def click_back_to_products_button(self):
        self.get_back_to_products_button().click()
        print("Возврат на страницу продуктов после окончательного подтверждения заказа кнопкой Back Home.")

    # Methods
    def back_to_products_page(self):
        self.get_screenshots("back_to_products_page")
        self.get_current_url()
        self.get_assert_current_url('https://www.saucedemo.com/checkout-complete.html')
        self.click_back_to_products_button()
