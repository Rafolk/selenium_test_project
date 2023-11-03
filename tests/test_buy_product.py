from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.back_to_products_page import BackProductsPage


def test_buy_product_1(driver):
    login = LoginPage(driver)
    login.authorization()

    add_and_go_to_cart = MainPage(driver)
    add_and_go_to_cart.methods_add_to_cart_product_1()

    confirm_order_in_cart = CartPage(driver)
    confirm_order_in_cart.confirm_cart_content()

    input_and_confirm_checkout_information = CheckoutInformationPage(driver)
    input_and_confirm_checkout_information.input_and_confirm_checkout_information()

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.finish_order()

    back_to_products_page = BackProductsPage(driver)
    back_to_products_page.back_to_products_page()


def test_buy_product_2(driver):
    login = LoginPage(driver)
    login.authorization()

    add_and_go_to_cart = MainPage(driver)
    add_and_go_to_cart.methods_add_to_cart_product_2()

    confirm_order_in_cart = CartPage(driver)
    confirm_order_in_cart.confirm_cart_content()

    input_and_confirm_checkout_information = CheckoutInformationPage(driver)
    input_and_confirm_checkout_information.input_and_confirm_checkout_information()

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.finish_order()

    back_to_products_page = BackProductsPage(driver)
    back_to_products_page.back_to_products_page()


def test_buy_product_3(driver):
    login = LoginPage(driver)
    login.authorization()

    add_and_go_to_cart = MainPage(driver)
    add_and_go_to_cart.methods_add_to_cart_product_3()

    confirm_order_in_cart = CartPage(driver)
    confirm_order_in_cart.confirm_cart_content()

    input_and_confirm_checkout_information = CheckoutInformationPage(driver)
    input_and_confirm_checkout_information.input_and_confirm_checkout_information()

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.finish_order()

    back_to_products_page = BackProductsPage(driver)
    back_to_products_page.back_to_products_page()
