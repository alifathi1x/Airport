from model.tools.validator import *

class FlyInformation:
    def __init__(self,id,fly_number,direction,destination,date_time,outrange_fly,status=True,):
        self.id = None
        self.fly_number = fly_number
        self.direction = direction
        self.destination = destination
        self.date_time = date_time
        self.status = status
        self.outrane_fly = outrane_fly

    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_fly_number(self):
        return self._fly_number
    def set_fly_number(self,fly_number):
        if isinstance(fly_number,bool):
            self._fly_number = fly_number
        else:
            raise ValueError("Invalid fly_number")

    def get_direction(self):
        return self._direction
    def set_direction(self,direction):
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
        if isinstance(date_time,int):
            self._date_time = date_time
        else:
            raise ValueError("Invalid date time")



