from data.months import Months


class Date:
    def __init__(self, day: str, month: str, year: str):
        self.day = day
        self.month = month
        self.year = year

    def as_str(self):
        return f'{self.day} {Months(self.month).name},{self.year}'
