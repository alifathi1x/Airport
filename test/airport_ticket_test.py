from model.da.da import DataAccess
from model.entity.fly_information import *
from controller.fly_controller import FlyController

controller = FlyController()
print(controller.save(6,"teh","shiraz",datetime.now(),True,True))
