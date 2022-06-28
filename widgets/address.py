from widgets.elements.select import Dropdown
from widgets.elements.textarea import Textarea


class AddressBlock:
    def __init__(self):
        """
        Представляет из себя мини-блок формы с полями Current Address и State and City
        """
        self.current_address = Textarea(selector='#currentAddress')
        self.state = Dropdown(selector='#state')
        self.city = Dropdown(selector='#city')

    def type_address(self, current):
        self.current_address.type(value=current)

    def select_state(self, state):
        self.state.select_by_text(text=state)

    def select_city(self, city):
        self.city.select_by_text(text=city)
