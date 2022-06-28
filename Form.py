from selene import be
from selene.support.shared import browser

from Address import Address
from Contacts import Contacts
from PersonInfo import PersonInfo


class PracticeForm:
    def __init__(self):
        self.contacts = Contacts()
        self.info = PersonInfo()
        self.address = Address()

    def submit(self):
        browser.element('#submit').should(be.visible).click()
