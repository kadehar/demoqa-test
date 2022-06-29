from selene import be
from selene.support.shared import browser

from data.date import Date
from widgets.elements.select import CustomSelect


class DatePicker:
    def __init__(self, selector):
        """
        Класс-обёртка, позволяющий работать с элементом как с календарём

        :param selector: селектор, по которому будет найден календарь
        """
        self.selector = selector

    def open(self):
        browser.find(self.selector).should(be.visible).click()

    def select_year(self, year: str):
        select = CustomSelect(selector='select[class*=year-select]')
        select.by_value(value=year)

    def select_month(self, month: str):
        select = CustomSelect(selector='select[class*=month-select]')
        select.by_value(value=month)

    def select_day(self, day: str):
        day_selector = f".//*[text()='{day}']"
        day_container = browser.element('div[class*=month][role=listbox]') \
            .element(day_selector)
        day_container.should(be.visible).click()

    def select_date(self, date: Date):
        self.open()
        self.select_year(date.year)
        self.select_month(date.month)
        self.select_day(date.day)
