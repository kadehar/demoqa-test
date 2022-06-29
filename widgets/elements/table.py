from selene.support.shared import browser


class Table:
    def __init__(self, root):
        """
        Класс-обёртка, позволяющий работать с элементом как с таблицей

        :param root: корневой элемент, по которому будет найдена вся таблица
        """
        self.table = browser.element(root)

    def body(self):
        return self.table.element('tbody')

    def rows(self):
        return self.body().all('tr')

    def cells(self):
        return self.body().all('td')

    def cell(self, cell_number: int):
        return self.cells()[cell_number]

    def row(self, row_number: int):
        return self.rows()[row_number]
