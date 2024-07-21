from controller.exeptions import CustomerNotFoundError
from model.da.da import DataAccess
from model.entity.customer_information import CustomerInformation
from model.tools.decorator import *

class CustomerService:
    @classmethod
    def save(cls,customer):
        customer_da = DataAccess(CustomerInformation)
        customer_da.save(customer)
        return customer

    @classmethod
    def edit(cls,customer):
        customer_da = DataAccess(CustomerInformation)
        if customer_da.find_by_id(customer.id):
            customer_da.edit(customer)
            return customer
        else:
            raise CustomerNotFoundError()

    @classmethod
    def remove(cls,customer):
        customer_da = DataAccess(CustomerInformation)
        if customer_da.find_by_id(customer.id):
            return customer_da.remove(id)
        else:
            raise CustomerNotFoundError()

    @classmethod
    def find_all(cls):
        customer_da = DataAccess(CustomerInformation)
        return customer_da.find_all()

    @classmethod
    def find_by_id(cls,id):
        customer_da = DataAccess(CustomerInformation)
        return customer_da.find_by_id(id)


    @classmethod
    def find_by_family(cls, family, customer):
        customer_da = DataAccess(CustomerInformation)
        return customer_da.find_by(customer.family == family)

    @classmethod
    def find_by_name(cls,name,customer):
        customer_da = DataAccess(CustomerInformation)
        return customer_da.find_by(customer.name == name)