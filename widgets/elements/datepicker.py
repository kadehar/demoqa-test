from selene import be
from selene.support.shared import browser

from widgets.elements.select import CustomSelect


class DatePicker:
    def __init__(self, day, month, year, element='#dateOfBirthInput'):
        self.day = day
        self.month = month
        self.year = year
        self.element = element

    def open(self):
        browser.find(self.element).should(be.visible).click()

    def select_year(self):
        select = CustomSelect(element='select[class*=year-select]')
        select.by_value(value=self.year)

    def select_month(self):
        select = CustomSelect(element='select[class*=month-select]')
        select.by_value(value=self.month)

    def select_day(self):
        day_selector = f".//*[text()='{self.day}']"
        day_container = browser.element('div[class*=month][role=listbox]') \
            .element(day_selector)
        day_container.should(be.visible).click()
