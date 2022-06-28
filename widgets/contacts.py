from widgets.elements.inputs import InputField


class ContactsBlock:
    def __init__(self):
        self.email = InputField(element="input[placeholder='name@example.com']")
        self.phone = InputField(element="input[placeholder='Mobile Number']")

    def type_email(self, mail):
        self.email.type(value=mail)

    def type_phone(self, number):
        self.phone.type(value=number)
