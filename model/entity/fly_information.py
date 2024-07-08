import datetime

from model.tools.validator import *
from sqlalchemy import column, Integer, String, DateTime, Boolean, Column
from sqlalchemy.orm import relationship
from model.entity.base import Base


class FlyInformation(Base):
    __tablename__ = "fly_information_tbl"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    fly_number = Column("fly_number", Integer, nullable=False, unique=True)
    direction = Column("direction", String(20), nullable=False)
    destination = Column("destination", String(20), nullable=False)
    date_time = Column("date_time", DateTime, nullable=False)
    fly_type = Column("fly_type", Boolean, nullable=False)
    status = Column("status", Boolean, nullable=False)

    def __init__(self, fly_number, direction, destination, date_time, fly_type, status):
        self.id = None
        self.fly_number = fly_number
        self.direction = direction
        self.destination = destination
        self.date_time = date_time
        self.status = status
        self.fly_number = fly_type

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_fly_number(self):
        return self._fly_number

    def set_fly_number(self, fly_number):
        if isinstance(fly_number, int):
            self._fly_number = fly_number
        else:
            raise ValueError("Invalid fly_number")

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        if name_validator(direction):
            self._direction = direction
        else:
            raise ValueError("Invalid direction")

    def get_destination(self):
        return self._destination

    def set_destination(self, destination):
        if name_validator(destination):
            self._destination = destination
        else:
            raise ValueError("Invalid destination")

    def get_date_time(self):
        return self._date_time

    def set_date_time(self, date_time):
        if isinstance(date_time, datetime.datetime):
            self._date_time = date_time
        else:
            raise ValueError("Invalid date time")

    def get_fly_type(self):
        return self._fly_number

    def set_fly_type(self, fly_type):
        if isinstance(fly_type, bool):
            self._fly_type = fly_type
        else:
            raise ValueError("Invalid out_range_fly")

    def get_status(self):
        return self._status

    def set_status(self, status):
        if isinstance(status, bool):
            self._status = status
        else:
            raise ValueError("Invalid status")

    fly_number = property(get_fly_number, set_fly_number)
    direction = property(get_direction, set_direction)
    destination = property(get_destination, set_destination)
    date_time = property(get_date_time, set_date_time)
    fly_type = property(get_fly_type, set_fly_type)
    status = property(get_status, set_status)
