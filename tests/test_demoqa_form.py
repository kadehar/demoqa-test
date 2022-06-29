from selene import have

from testdata.user import prepare_default_user
from widgets.elements.table import Table
from widgets.form import PracticeForm

form = PracticeForm()
profile = prepare_default_user()
phone = profile.phone()


def test_practice_form():
    form.profile.set_name(profile.name)
    form.contacts.type_email(profile.email())
    form.profile.select_gender(profile.gender)
    form.contacts.type_phone(phone)
    form.profile.select_date_of_birth(profile.birthday)
    form.profile.add_subjects(profile.categories)
    form.profile.select_hobbies(profile.hobbies)
    form.profile.upload_avatar(profile.avatar.full_path())
    form.address.type_address(profile.address.full_address())
    form.address.select_state(profile.address.state)
    form.address.select_city(profile.address.city)
    form.submit_button.click()

    table = Table(root='.modal-body > .table-responsive > .table')
    table.cell(1).should(have.text(profile.name.full_name()))
    table.cell(3).should(have.text(profile.email()))
    table.cell(5).should(have.text(profile.gender))
    table.cell(7).should(have.text(phone))
    table.cell(9).should(have.text(profile.birthday.as_str()))
    table.cell(11).should(have.text(profile.categories.to_str()))
    table.cell(13).should(have.text(profile.hobbies.to_str()))
    table.cell(15).should(have.text(profile.avatar.file))
    table.cell(17).should(have.text(profile.address.full_address()))
    table.cell(19).should(have.text(profile.address.state_and_city()))
