from widgets.elements.select import Dropdown
from widgets.elements.textarea import Textarea


class AddressBlock:
    def __init__(self):
        self.current_address = Textarea(element='#currentAddress')
        self.state = Dropdown(element='#state')
        self.city = Dropdown(element='#city')

    def type_address(self, current):
        self.current_address.type(value=current)

    def select_state(self, state):
        self.state.select_by_text(text=state)

    def select_city(self, city):
        self.city.select_by_text(text=city)
