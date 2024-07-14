
from model.da.da import DataAccess
from model.entity.fly_information import *

fly = FlyInformation(2222,"tehran","aaa",datetime.now(),True,True)
fly_da = DataAccess(FlyInformation)
fly_da.save(fly)

print(fly)