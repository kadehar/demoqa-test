from selene import be
from selene.support.shared import browser

from Select import CustomSelect


class DatePicker:
    """
    Represents DatePicker element for user-friendly date select
    """

    def __init__(self, element, day, month, year):
        """
        :param day: from 1 to 31
        :param month: from 0 to 11
        :param year: from 19xx till now
        """
        self.day = day
        self.month = month
        self.year = year
        self.element = element

    def open(self):
        browser.find(self.element).should(condition=be.visible, timeout=10).click()

    def select_year(self):
        year_select = CustomSelect(element='select[class*=year-select]')
        year_select.by_value(value=self.year)

    def select_month(self):
        month_select = CustomSelect(element='select[class*=month-select]')
        month_select.by_value(value=self.month)

    def select_day(self):
        day_selector = f".//*[text()='{self.day}']"
        day_container = browser.element('div[class*=month][role=listbox]') \
            .element(day_selector)
        day_container.should(be.visible).click()
