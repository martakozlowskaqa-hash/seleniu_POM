from faker import Faker
from utils.custom_types import Gender
import random

class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER = random.choice([Gender.MALE, Gender.FEMALE])
        self.fake = Faker("pl_PL")
        if self.GENDER == Gender.FEMALE:
            self.FIRST_NAME = self.fake.first_name_female()
        else:
            self.FIRST_NAME = self.fake.first_name_male()
        self.EMAIL = self.fake.email()
        #zdeklarowanie hasla min 5 do 10 znakow
        self.PASSWORD = self.fake.password(int(random.random() * 6) + 5)
        self.DATE_OF_BIRTH = self.fake.date_of_birth()
        self.LAST_NAME = self.fake.last_name()