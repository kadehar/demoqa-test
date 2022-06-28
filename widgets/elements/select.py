from selene import be
from selenium.webdriver.support.select import Select
from selene.support.shared import browser


class CustomSelect:
    def __init__(self, element):
        self.element = element

    def by_value(self, value):
        select = Select(browser.driver.find_element_by_css_selector(self.element))
        select.select_by_value(value=value)


class Dropdown:
    def __init__(self, element):
        self.element = element

    def select_by_text(self, text):
        text_selector = f"//*[text()='{text}']"
        dropdown = browser.element(self.element).should(be.visible)
        dropdown.click()
        browser.element(text_selector).should(be.visible).click()
