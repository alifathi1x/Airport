from model.da.da import DataAccess
from model.entity.customer_information import *
from datetime import datetime

my_date = datetime.now()

customer = CustomerInformation("ali","abolfathi",my_date,"999999999","9999999")
customer_da = DataAccess(CustomerInformation)
customer_da.save(customer)
print(customer)