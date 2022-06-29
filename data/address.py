class Address:
    def __init__(self, state, city, street, house, flat):
        self.state = state
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def full_address(self):
        return f'{self.state}, {self.city}, {self.street} {self.house}-{self.flat}'

    def state_and_city(self):
        return f'{self.state} {self.city}'
