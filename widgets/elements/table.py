from selene.support.shared import browser


class Table:
    def __init__(self, root='.table'):
        """
        Класс-обёртка, позволяющий работать с элементом как с таблицей

        :param root: корневой элемент, по которому будет найдена вся таблица
        """
        self.table = browser.element(root)

    def body(self):
        return self.table.element('tbody')

    def rows(self):
        return self.body().ss('tr')

    def cells(self):
        return self.body().ss('td')
