import datetime
import os


class Base:

    def __init__(self, driver):
        self.driver = driver

    """"Метод для получения текущей url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"\nТекущая url - {get_url}.")

    """"Метод для получения и сравнения текста"""
    def get_assert_text(self, actual, expected):
        actual_text = actual.text
        assert actual_text == expected
        print(f"\nОжидаемый текст совпадает с фактическим.")

    """"Метод для создания скриншотов"""
    def get_screenshots(self, name_file):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y__%H-%M-%S")
        if not os.path.isdir("./screenshots_for_check_tests"):
            os.mkdir("./screenshots_for_check_tests")
        self.driver.save_screenshot(f'./screenshots_for_check_tests/{name_file}_{now_date}.png')
        print(f"\nОжидаемый текст совпадает с фактическим.")

    """"Метод для получения и сравнения текущей url"""
    def get_assert_current_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url
        print(f"\nОжидаемая url совпадает с фактической.")
