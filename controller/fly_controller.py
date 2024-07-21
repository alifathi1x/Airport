from model.entity.fly_information import FlyInformation
from model.service.fly_service import FlyService
from model.tools.decorator import exception_handling

class FlyController:
    @classmethod
    @exception_handling
    def save(cls,fly_number, direction, destination, date_time, fly_type, status):
        fly = FlyInformation(fly_number, direction, destination, date_time, fly_type, status)
        return True, FlyService.save(fly)

    @classmethod
    @exception_handling
    def edit(cls,fly_number, direction, destination, date_time, fly_type,status):
        fly = FlyInformation(fly_number, direction, destination, date_time, fly_type,status)
        fly.id = id
        return True, FlyService.edit(fly)

    @classmethod
    @exception_handling
    def remove(cls,id):
        return True, FlyService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, FlyService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, FlyService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_fly_number(cls, fly_number):
        return True, FlyService.find_by_fly_number(fly_number)
