from selene import be
from selene.support.shared import browser


class FileInput:
    def __init__(self, element):
        self.element = element

    def upload(self, file):
        browser.element(css_or_xpath_or_by=self.element).type(file)


class InputField:
    def __init__(self, element):
        self.input_field = browser.element(css_or_xpath_or_by=element)

    def type(self, value):
        self.input_field.should(be.visible).type(value)

    def type_and_press_enter(self, value):
        self.type(value=value)
        self.input_field.press_enter()
