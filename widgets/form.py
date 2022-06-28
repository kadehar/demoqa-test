from widgets.address import AddressBlock
from widgets.contacts import ContactsBlock
from widgets.elements.button import Button
from widgets.profile import ProfileBlock


class PracticeForm:
    def __init__(self):
        """
        Представляет из себя Practice Form, состоящую из мини-блоков Contacts, Address и Profile
        """
        self.submit_button = Button(selector='#submit')
        self.contacts = ContactsBlock()
        self.address = AddressBlock()
        self.profile = ProfileBlock()
