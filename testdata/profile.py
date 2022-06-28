import os

from enums.gender import Gender
from enums.hobbies import Hobbies
from enums.months import Months
from enums.subjects import Subjects


class Profile:
    FIRST_NAME = 'John'
    LAST_NAME = 'Richardson'
    GENDER = Gender.MALE.value
    SUBJECTS = (Subjects.MATHS, Subjects.ENGLISH)
    HOBBIES = (Hobbies.READING, Hobbies.MUSIC)
    AVATAR = os.getcwd() + '/pic.jpg'


class Contacts:
    EMAIL = 'john.richardson@yahoo.com'
    PHONE = '9999999999'


class Birthday:
    DAY = '20'
    MONTH = Months.NOVEMBER.value
    YEAR = '1965'
