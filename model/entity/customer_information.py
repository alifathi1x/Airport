from model.tools.validator import *
from sqlalchemy import column, Integer, String, Boolean, Column
from sqlalchemy.orm import relationship
from model.entity import *


class CustomerInformation(Base):
    __tablename__ = "customer_information_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30), nullable=False)
    _birth_date = Column("BirthDate", Integer, nullable=False, unique=True)
    _national_id = Column("national ID", Integer, nullable=False, unique=True)
    _passport_number = Column("passport_ID", Integer, nullable=False, unique=True)

    def __init__(self, name, family, birth_date, national_id, passport_number):
        self.id = None
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.national_id = national_id
        self.passport_number = passport_number

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name_validator(name):
            self._name = name
        else:
            raise ValueError("Invalid Name")

    def get_family(self):
        return self._family

    def set_family(self, family):
        if name_validator(family):
            self._family = family
        else:
            raise ValueError("Invalid Family")

    def get_birth_date(self):
        return self._birth_date

    def set_birth_date(self, birth_date):
        if isinstance(birth_date, int):
            self._birth_date = birth_date
        else:
            raise ValueError("Invalid Birthday Input")

    def get_national_id(self):
        return self._national_id

    def set_national_id(self, national_id):
        if national_id_validator(national_id):
            self._national_id = national_id
        else:
            raise ValueError("Invalid National ID")

    def get_passport_number(self):
        return self._passport_number

    def set_passport_number(self, passport_number):
        if isinstance(passport_number, int) and passport_validator(passport_number):
            self._passport_number = passport_number
        else:
            raise ValueError("Invalid Passport Number")

    name = property(get_name, set_name)
    family = property(get_family, set_family)
    birth_date = property(get_birth_date, set_birth_date)
    national_id = property(get_national_id, set_national_id)
    passport_number = property(get_passport_number, set_passport_number)
