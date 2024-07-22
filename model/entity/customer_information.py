from datetime import date
from model.tools.validator import *
from sqlalchemy import Integer, String, Column, Date
from model.entity.base import Base


class CustomerInformation(Base):
    __tablename__ = "customer_information_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _birth_date = Column("birth_date", Date, nullable=False)
    _national_id = Column("national_id", Integer, nullable=False, unique=True)
    _passport_number = Column("passport_number", Integer, nullable=False, unique=True)

    def __init__(self, name, family, birth_date, national_id, passport_number):
        self._id = None
        self._name = name
        self._family = family
        self._birth_date = birth_date
        self._national_id = national_id
        self._passport_number = passport_number

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
        if isinstance(birth_date, date):
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
        if isinstance(passport_number, int):
            self._passport_number = passport_number
        else:
            raise ValueError("Invalid Passport Number")

    id = property(get_id,set_id)
    name = property(get_name, set_name)
    family = property(get_family, set_family)
    birth_date = property(get_birth_date, set_birth_date)
    national_id = property(get_national_id, set_national_id)
    passport_number = property(get_passport_number, set_passport_number)
