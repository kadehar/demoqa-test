from selene import be
from selene.support.shared import browser


class Input:
    """
    Input-wrapper for user-friendly text/file input by element
    """

    def __init__(self, element):
        self.input_field = browser.element(css_or_xpath_or_by=element)

    def set_value_and_press_enter(self, value):
        self.set_value(value=value)
        self.input_field.press_enter()

    def set_value(self, value):
        self.input_field.should(be.visible).type(value)

    def set_file(self, file):
        self.input_field.type(file)
