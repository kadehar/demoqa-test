from selene import have

from testdata.address import Address
from testdata.expected import Expected
from testdata.profile import Profile, Contacts, Birthday
from widgets.elements.table import Table
from widgets.form import PracticeForm

form = PracticeForm()


def test_practice_form(open_practice_form):
    form.profile.set_name(first_name=Profile.FIRST_NAME, last_name=Profile.LAST_NAME)
    form.contacts.type_email(mail=Contacts.EMAIL)
    form.profile.select_gender(gender=Profile.GENDER)
    form.contacts.type_phone(number=Contacts.PHONE)
    form.profile.select_date_of_birth(date=Birthday)
    form.profile.set_subjects(*Profile.SUBJECTS)
    form.profile.select_hobbies(*Profile.HOBBIES)
    form.profile.upload_avatar(file=Profile.AVATAR)
    form.address.type_address(current=Address.ADDRESS)
    form.address.select_state(state=Address.STATE)
    form.address.select_city(city=Address.CITY)
    form.submit_button.click()

    Table().rows().should(have.texts(
        Expected.NAME,
        Contacts.EMAIL,
        Profile.GENDER,
        Contacts.PHONE,
        Expected.DATE_OF_BIRTH,
        Expected.SUBJECTS,
        Expected.HOBBIES,
        Expected.PICTURE,
        Address.ADDRESS,
        Expected.STATE_AND_CITY
    ))
