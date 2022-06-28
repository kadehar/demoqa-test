from widgets.address import AddressBlock
from widgets.contacts import ContactsBlock
from widgets.elements.button import Button
from widgets.profile import ProfileBlock


class PracticeForm:
    def __init__(self):
        self.submit_button = Button(element='#submit')
        self.contacts = ContactsBlock()
        self.address = AddressBlock()
        self.profile = ProfileBlock()
