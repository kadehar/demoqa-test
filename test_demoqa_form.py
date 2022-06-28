import os

from TestData import TestData
from Form import PracticeForm

avatar = os.getcwd() + '/pic.jpg'
form = PracticeForm()


def test_practice_form(open_practice_form):
    form.info.set_name(first_name=TestData.FIRST_NAME, last_name=TestData.LAST_NAME)
    form.contacts.set_email(mail=TestData.EMAIL)
    form.info.set_gender(gender=TestData.GENDER)
    form.contacts.set_phone(phone_number=TestData.MOBILE_PHONE)
    form.info.set_birth_date(day=TestData.DAY_OF_BIRTH, month=TestData.MONTH_OF_BIRTH, year=TestData.YEAR_OF_BIRTH)
    form.info.set_subjects(TestData.SUBJECT_MATHS, TestData.SUBJECT_ENGLISH)
    form.info.set_hobbies(TestData.HOBBY_READING, TestData.HOBBY_MUSIC)
    form.info.set_avatar(avatar=avatar)
    form.address.set_current(address=TestData.CURRENT_ADDRESS)
    form.address.set_state(state=TestData.STATE)
    form.address.set_city(city=TestData.CITY)
    form.submit()




