from selene.support.conditions.have import texts
from selene.support.shared import browser


class Table:
    def __init__(self, root):
        self.table = browser.element(root)

    def body(self):
        return self.table.element('tbody')

    def rows(self):
        return self.body().ss('tr')
