from selene import be
from selene.support.shared import browser


class Checkbox:
    def __init__(self, root):
        """
        Класс-обёртка, позволяющий работать с элементом как с чекбоксом

        :param root: корневой элемент, которому принадлежит чекбокс
        """
        self.root = root

    def select_by_text(self, text):
        selector = f"//*[text()='{text}']"
        browser.element(self.root).should(be.visible).element(selector).click()
