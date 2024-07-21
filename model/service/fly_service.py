from controller.exeptions import FlyNotFoundError
from model.da.da import DataAccess
from model.entity.fly_information import FlyInformation
from model.tools.decorator import *

class FlyService:
    @classmethod
    def save(cls,fly):
        fly_da = DataAccess(FlyInformation)
        fly_da.save(fly)
        return fly

    @classmethod
    def edit(cls,fly):
        fly_da = DataAccess(FlyInformation)
        if fly_da.find_by_id(fly.id):
            fly_da.edit(fly)
            return fly
        else:
            raise FlyNotFoundError()

    @classmethod
    def remove(cls,id):
        fly_da = DataAccess(FlyInformation)
        if fly_da.find_by_id(id):
            fly_da.remove(id)
        else:
            raise FlyNotFoundError()

    @classmethod
    def findd_all(cls):
        fly_da = DataAccess(FlyInformation)
        return fly_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        fly_da = DataAccess(FlyInformation)
        return fly_da.find_by_id(id)

    @classmethod
    def find_by_fly_number(cls, fly_number):
        fly_da = DataAccess(FlyInformation)
        return fly_da.find_by(fly_number.fly_number == fly_number)