from selene import be
from selene.support.shared import browser


class Textarea:
    def __init__(self, element):
        self.element = element

    def set_value(self, value):
        browser.element(css_or_xpath_or_by=self.element).should(be.visible).type(value)
