from selene import be
from selene.support.shared import browser

from data.date import Date
from data.profile import Name, Categories, Hobbies
from widgets.elements.checkbox import Checkbox
from widgets.elements.datepicker import DatePicker
from widgets.elements.inputs import FileInput, InputField
from widgets.elements.radiobutton import RadioButton


class ProfileBlock:
    def __init__(self):
        """
        Представляет из себя мини-блок формы с полями Name, Gender, Date of Birth,
        Subjects, Hobbies и Picture
        """
        self.birthday_picker = DatePicker(selector='#dateOfBirthInput')
        self.gender_radio = RadioButton(root='#genterWrapper')
        self.hobbies_wrapper = Checkbox(root='#hobbiesWrapper')
        self.avatar = FileInput(selector='#uploadPicture')
        self.first_name = InputField(selector="input[placeholder='First Name']")
        self.last_name = InputField(selector="input[placeholder='Last Name']")
        self.subjects_input = InputField(selector="#subjectsInput")

    def select_gender(self, gender):
        self.gender_radio.select_by_text(gender)

    def select_hobbies(self, hobbies: Hobbies):
        for hobby in hobbies.to_list():
            self.hobbies_wrapper.select_by_text(hobby)

    def upload_avatar(self, file):
        self.avatar.upload(file)

    def add_subjects(self, categories: Categories):
        subjects_input_container = browser.element('div[class*=value-container]')
        subjects_input_container.should(be.visible).click()
        for category in categories.to_list():
            self.subjects_input.type_and_press_enter(category)

    def select_date_of_birth(self, date: Date):
        self.birthday_picker.select_date(date)

    def set_name(self, name: Name):
        self.first_name.type(value=name.first_name)
        self.last_name.type(value=name.last_name)
