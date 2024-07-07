from model.tools.validator import *

class FlyInformation:
    def __init__(self,id,fly_number,direction,destination,date_time,out_range_fly,status=True,):
        self.id = None
        self.fly_number = fly_number
        self.direction = direction
        self.destination = destination
        self.date_time = date_time
        self.status = status
        self.out_range_fly = out_range_fly

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

    def get_out_range_fly(self):
        return self._get_out_range_fly
    def set_out_range_fly(self,out_range_fly):
        if out_range_fly == True:
            self._out_range_fly = out_range_fly
        else:
            raise ValueError("Invalid out_range_fly")

    def get_status(self):
        return self._status
    def set_status(self, status):
        if isinstance(status,bool):
            self._status = status
        else:
            raise ValueError("Invalid status")


    fly_number = property(get_fly_number,set_fly_number)
    direction = property(get_direction,set_direction)
    destination = property(get_destination,set_destination)
    date_time = property(get_date_time,set_date_time)
    out_range_fly = property(get_out_range_fly,set_out_range_fly)
    status = property(get_status,set_status)



