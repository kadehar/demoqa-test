from selene import be
from selene.support.shared import browser

from enums.hobbies import Hobbies
from enums.subjects import Subjects
from testdata.profile import Birthday
from widgets.elements.checkbox import Checkbox
from widgets.elements.datepicker import DatePicker
from widgets.elements.inputs import FileInput, InputField
from widgets.elements.radiobutton import RadioButton


class ProfileBlock:
    """
    Представляет из себя мини-блок формы с полями Name, Gender, Date of Birth,
    Subjects, Hobbies и Picture
    """

    def select_gender(self, gender):
        RadioButton(text=gender).select()

    def select_hobbies(self, *hobbies: Hobbies):
        for hobby in hobbies:
            Checkbox(text=hobby.value).select()

    def upload_avatar(self, file):
        FileInput(selector='#uploadPicture').upload(file=file)

    def select_date_of_birth(self, date: Birthday):
        birth_date_picker = DatePicker(day=date.DAY, month=date.MONTH, year=date.YEAR)
        birth_date_picker.open()
        birth_date_picker.select_year()
        birth_date_picker.select_month()
        birth_date_picker.select_day()

    def set_subjects(self, *subjects: Subjects):
        subjects_input_container = browser.element('div[class*=value-container]')
        subjects_input_container.should(be.visible).click()
        subjects_input = InputField(selector="#subjectsInput")

        for subject in subjects:
            subjects_input.type_and_press_enter(value=subject.value)

    def set_name(self, first_name, last_name):
        InputField(selector="input[placeholder='First Name']").type(value=first_name)
        InputField(selector="input[placeholder='Last Name']").type(value=last_name)
