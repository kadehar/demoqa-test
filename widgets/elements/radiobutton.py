from selene import be
from selene.support.shared import browser


class RadioButton:
    def __init__(self, text):
        self.text = text

    def select(self):
        label = f"//label[text()='{self.text}']"
        browser.element(css_or_xpath_or_by=label).should(be.visible).click()
