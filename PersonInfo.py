from selene import be
from selene.support.shared import browser

from Checkbox import Checkbox
from DatePicker import DatePicker
from Hobbies import Hobbies
from RadioButton import RadioButton
from Input import Input
from Subjects import Subjects


class PersonInfo:
    def __init__(self):
        self.first_name = Input(element="input[placeholder='First Name']")
        self.last_name = Input(element="input[placeholder='Last Name']")
        self.subjects_input = Input(element="#subjectsInput")

    def set_gender(self, gender):
        RadioButton(text=gender).toggle()

    def set_hobbies(self, *hobbies: Hobbies):
        for hobby in hobbies:
            Checkbox(text=hobby.value).toggle()

    def set_subjects(self, *subjects: Subjects):
        browser.element('div[class*=value-container]').should(be.visible).click()
        for subject in subjects:
            self.subjects_input.set_value_and_press_enter(value=subject.value)

    def set_name(self, first_name, last_name):
        self.first_name.set_value(value=first_name)
        self.last_name.set_value(value=last_name)

    def set_avatar(self, avatar):
        Input(element='#uploadPicture').set_file(file=avatar)

    def set_birth_date(self, day, month, year):
        birth_date_picker = DatePicker(element='#dateOfBirthInput', day=day, month=month, year=year)
        birth_date_picker.open()
        birth_date_picker.select_year()
        birth_date_picker.select_month()
        birth_date_picker.select_day()
