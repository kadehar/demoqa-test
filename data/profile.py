import os
import random

from data.address import Address
from data.date import Date
from data.gender import Gender
from data.hobby import Hobby
from data.subject import Subject


class Categories:
    def __init__(self, *categories: Subject):
        self.categories = categories

    def to_list(self):
        return tuple(category.value for category in self.categories)

    def to_str(self):
        return ', '.join(self.to_list())


class Hobbies:
    def __init__(self, *hobbies: Hobby):
        self.hobbies = hobbies

    def to_list(self):
        return tuple(hobby.value for hobby in self.hobbies)

    def to_str(self):
        return ', '.join(self.to_list())


class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Avatar:
    def __init__(self, file, path=None):
        self.path = path or f"{os.path.abspath('../resources/')}"
        self.file = file

    def full_path(self):
        return f'{self.path}/{self.file}'


class Profile:
    def __init__(self, name: Name, gender: Gender, avatar: Avatar, birthday: Date,
                 categories: Categories, hobbies: Hobbies, address: Address):
        self.categories = categories
        self.hobbies = hobbies
        self.name = name
        self.gender = gender.value
        self.avatar = avatar
        self.birthday = birthday
        self.address = address

    def email(self, domain=None):
        return f'{self.name.first_name}.{self.name.last_name}@{domain or "yahoo.com"}'

    def phone(self):
        phone = [str(random.randint(0, 9)) for _ in range(10)]
        return ''.join(phone)
