import random

from data.address import Address
from data.date import Date
from data.gender import Gender
from data.hobby import Hobby
from data.months import Months
from data.profile import Name, Categories, Hobbies, Profile, Avatar
from data.subject import Subject


def prepare_default_user():
    day = str(random.randint(1, 25))
    month: Months = random.choice(list(Months))
    year = str(random.randint(1956, 2000))

    birthday = Date(day=day, month=month.value, year=year)
    name = Name(first_name='John', last_name='Richardson')
    gender: Gender = random.choice(list(Gender))
    avatar = Avatar(file='pic.jpg')
    categories = Categories(Subject.Maths, Subject.English)
    hobbies = Hobbies(Hobby.Reading, Hobby.Music)
    address = Address(state='NCR', city='Noida', street='Banagalada st.', house='15', flat='1')
    profile = Profile(name=name, gender=gender, avatar=avatar, categories=categories,
                      hobbies=hobbies, birthday=birthday, address=address)

    return profile
