from selene.support.conditions.have import texts

from Form import PracticeForm
from Table import Table
from TestData import TestData

form = PracticeForm()


def test_practice_form(open_practice_form):
    form.info.set_name(first_name=TestData.FIRST_NAME, last_name=TestData.LAST_NAME)
    form.contacts.set_email(mail=TestData.EMAIL)
    form.info.set_gender(gender=TestData.GENDER)
    form.contacts.set_phone(phone_number=TestData.MOBILE_PHONE)
    form.info.set_birth_date(day=TestData.DAY_OF_BIRTH,
                             month=TestData.MONTH_OF_BIRTH,
                             year=TestData.YEAR_OF_BIRTH)
    form.info.set_subjects(TestData.SUBJECT_MATHS, TestData.SUBJECT_ENGLISH)
    form.info.set_hobbies(TestData.HOBBY_READING, TestData.HOBBY_MUSIC)
    form.info.set_avatar(avatar=TestData.AVATAR)
    form.address.set_current(address=TestData.ADDRESS)
    form.address.set_state(state=TestData.STATE)
    form.address.set_city(city=TestData.CITY)
    form.submit()

    table = Table(root='.modal-body > .table-responsive > .table')
    table.rows().should_have(texts(TestData.EXPECTED_NAME,
                                   TestData.EMAIL,
                                   TestData.GENDER,
                                   TestData.MOBILE_PHONE,
                                   TestData.EXPECTED_DATE_OF_BIRTH,
                                   TestData.EXPECTED_SUBJECTS,
                                   TestData.EXPECTED_HOBBIES,
                                   TestData.EXPECTED_PICTURE,
                                   TestData.ADDRESS,
                                   TestData.EXPECTED_STATE_AND_CITY))
