from selene import be
from selene.support.shared import browser
from selenium.webdriver.support.select import Select


class CustomSelect:
    def __init__(self, element):
        self.element = element

    def by_value(self, value):
        select = Select(browser.driver.find_element_by_css_selector(self.element))
        select.select_by_value(value=value)

    def by_text(self, text):
        text_selector = f"//*[text()='{text}']"
        select = browser.find(self.element).should(be.visible)
        select.click()
        browser.element(text_selector).should(be.visible).click()
