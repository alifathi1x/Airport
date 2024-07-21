from model.da.da import DataAccess
from model.entity.customer_information import *

customer = CustomerInformation("ali","abolfathi","22",999999999,9999999)
customer_da = DataAccess(CustomerInformation)
customer_da.save(customer)
print(customer)