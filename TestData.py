import os

from Gender import Gender
from Hobbies import Hobbies
from Months import Months
from Subjects import Subjects


class TestData:
    FIRST_NAME = 'John'
    LAST_NAME = 'Richardson'
    EMAIL = 'john.richardson@yahoo.com'
    GENDER = Gender.MALE.value
    MOBILE_PHONE = '9999999999'
    DAY_OF_BIRTH = '20'
    MONTH_OF_BIRTH = Months.NOVEMBER.value
    YEAR_OF_BIRTH = '1965'
    SUBJECTS = (Subjects.MATHS, Subjects.ENGLISH)
    HOBBIES = (Hobbies.READING, Hobbies.MUSIC)
    AVATAR = os.getcwd() + '/pic.jpg'
    ADDRESS = 'USA, New-York, 15 ave. 17'
    STATE = 'NCR'
    CITY = 'Noida'

    EXPECTED_NAME = 'John Richardson'
    EXPECTED_DATE_OF_BIRTH = '20 November,1965'
    EXPECTED_SUBJECTS = 'Maths, English'
    EXPECTED_HOBBIES = 'Reading, Music'
    EXPECTED_PICTURE = 'pic.jpg'
    EXPECTED_STATE_AND_CITY = 'NCR Noida'
