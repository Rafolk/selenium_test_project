

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
