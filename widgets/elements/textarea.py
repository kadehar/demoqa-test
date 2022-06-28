from selene import be
from selene.support.shared import browser


class Textarea:
    def __init__(self, selector):
        """
        Класс-обёртка, позволяющий работать с элементом как с текстовой областью

        :param selector: селектор, по которому будет найдена текстовая область
        """
        self.selector = selector

    def type(self, value):
        browser.element(css_or_xpath_or_by=self.selector).should(be.visible).type(value)
