from selene import be
from selene.support.shared import browser


class Button:
    def __init__(self, element):
        self.element = element

    def click(self):
        browser.element(css_or_xpath_or_by=self.element).should(be.visible).click()
