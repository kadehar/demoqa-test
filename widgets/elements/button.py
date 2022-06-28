from selene import be
from selene.support.shared import browser


class Button:
    def __init__(self, selector):
        """
        Класс-обёртка, позволяющий работать с элементом как с кнопкой

        :param selector: селектор, по которому будет найден элемент для взаимодействия
        """
        self.selector = selector

    def click(self):
        browser.element(css_or_xpath_or_by=self.selector).should(be.visible).click()
