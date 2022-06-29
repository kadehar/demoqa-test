from selene import be
from selene.support.shared import browser


class RadioButton:
    def __init__(self, root):
        """
        Класс-обёртка, позволяющий работать с элементом как с радиобаттоном

        :param root: корневой элемент, которому принадлежит радиобаттон
        """
        self.root = root

    def select_by_text(self, text):
        selector = f"//*[text()='{text}']"
        browser.element(self.root).should(be.visible).element(selector).click()
