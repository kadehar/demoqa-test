import os


class TestData:
    FIRST_NAME = 'John'
    LAST_NAME = 'Richardson'
    EMAIL = 'john.richardson@yahoo.com'
    GENDER = 'Male'
    MOBILE_PHONE = '9999999999'
    DAY_OF_BIRTH = '20'
    MONTH_OF_BIRTH = '10'  # November
    YEAR_OF_BIRTH = '1965'
    SUBJECT_MATHS = 'Maths'
    SUBJECT_ENGLISH = 'English'
    HOBBY_READING = 'Reading'
    HOBBY_MUSIC = 'Music'
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
