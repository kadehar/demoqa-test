from Input import Input


class Contacts:
    """
    Provide user-friendly input for e-mail and phone on form
    """
    def __init__(self):
        self.email = Input(element="input[placeholder='name@example.com']")
        self.phone = Input(element="input[placeholder='Mobile Number']")

    def set_email(self, mail):
        self.email.set_value(value=mail)

    def set_phone(self, phone_number):
        self.phone.set_value(value=phone_number)
