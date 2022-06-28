from selene import be
from selene.support.shared import browser


class Checkbox:
    def __init__(self, text):
        """
        Класс-обёртка, позволяющий работать с элементом как с чекбоксом

        :param text: текст, по которому будет найден чекбокс
        """
        self.text = f"//*[text()='{text}']"

    def select(self):
        browser.element(css_or_xpath_or_by=self.text).should(be.visible).click()
