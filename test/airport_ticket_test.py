from model.da.da import DataAccess
from model.entity.customer_information import *

d = date(2023, 3, 2)

customer = CustomerInformation("aaaa", "tehran",date.day, "1231231231", 111111111,)
customer_da = DataAccess(CustomerInformation)
customer_da.save(customer)

print(customer)
