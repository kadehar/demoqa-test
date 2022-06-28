from Select import CustomSelect
from Textarea import Textarea


class Address:
    def set_current(self, address):
        Textarea(element='#currentAddress').set_value(value=address)

    def set_state(self, state):
        CustomSelect(element='#state').by_text(text=state)

    def set_city(self, city):
        CustomSelect(element='#city').by_text(text=city)
