from model.da.da import DataAccess
from model.entity.customer_information import *
from datetime import datetime
d = datetime.now()

customer = CustomerInformation("ali","abolfathi",d,"899999999","9999999")
customer_da = DataAccess(CustomerInformation)
customer_da.save(customer)
print(customer)