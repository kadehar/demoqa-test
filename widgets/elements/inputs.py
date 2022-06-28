from selene import be
from selene.support.shared import browser


class FileInput:
    def __init__(self, selector):
        """
        Класс-обёртка, позволяющий работать с элементом как с полем загрузки файла

        :param selector: селектор, по которому будет найдено поле загрузки
        """
        self.selector = selector

    def upload(self, file):
        browser.element(css_or_xpath_or_by=self.selector).type(file)


class InputField:
    def __init__(self, selector):
        """
        Класс-обёртка, позволяющий работать с элементом как с полем ввода

        :param selector: селектор, по которому будет найдено поле ввода
        """
        self.input_field = browser.element(css_or_xpath_or_by=selector)

    def type(self, value):
        self.input_field.should(be.visible).type(value)

    def type_and_press_enter(self, value):
        self.type(value=value)
        self.input_field.press_enter()
