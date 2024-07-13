from controller.exeptions import FlyNotFoundError
from model.da.da import DataAccess
from model.entity.fly_information import FlyInformation

class FlyService:
    @staticmethod
    def save(fly_information):
        fly_da = DataAccess(FlyInformation)
        fly_da.save(fly_information)
        return fly_information

    @staticmethod
    def edit(fly_information):
        fly_da = DataAccess(FlyInformation)
        if fly_da.find_by_id(fly_information.id):
            fly_da.edit(fly_information)
            return fly_information
        else:
            raise FlyNotFoundError()

    @staticmethod
    def remove(fly_information):
        fly_da = DataAccess(FlyInformation)
        if fly_da.find_by_id(fly_information):
            return fly_da.remove(fly_information)
        else:
            raise FlyNotFoundError()

    @staticmethod
    def find_all():
        fly_da = DataAccess(FlyInformation)
        return fly_da.find_all()

    @staticmethod
    def find_by_id(fly_information):
        fly_da = DataAccess(FlyInformation)
        return fly_da.find_by_id(fly_information)

    @staticmethod
    def find_by_fly_number(fly_number):
        fly_da = DataAccess(FlyInformation)
        return fly_da.find_by(FlyInformation.fly_number == fly_number)


