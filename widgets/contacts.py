from widgets.elements.inputs import InputField


class ContactsBlock:
    def __init__(self):
        """
        Представляет из себя мини-блок формы с полями Email и Mobile
        """
        self.email = InputField(selector="input[placeholder='name@example.com']")
        self.phone = InputField(selector="input[placeholder='Mobile Number']")

    def type_email(self, mail):
        self.email.type(value=mail)

    def type_phone(self, number):
        self.phone.type(value=number)
