from controller.exeptions import CustomerNotFoundError
from model.da.da import DataAccess
from model.entity.customer_information import CustomerInformation

class CustomerService:
    @staticmethod
    def save(customer):
        customer_da = DataAccess(CustomerInformation)
        customer_da.save(customer)
        return customer

    @staticmethod
    def edit(customer):
        customer_da = DataAccess(CustomerInformation)
        if customer_da.find_by_id(customer.id):
            customer_da.edit(customer)
            return customer
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def remove(customer):
        customer_da = DataAccess(CustomerInformation)
        if customer_da.find_by_id(customer):
            return customer_da.remove(customer)
        else:
            raise CustomerNotFoundError()

    @staticmethod
    def find_all():
        customer_da = DataAccess(CustomerInformation)
        return customer_da.find_all()

    @staticmethod
    def find_by_id(id):
        customer_da = DataAccess(CustomerInformation)
        return customer_da.find_by_id(id)

    @staticmethod
    def find_by_name(name):
        customer_da = DataAccess(CustomerInformation)
        return customer_da.find_by(CustomerInformation.name == name)

    @staticmethod
    def find_by_family(family):
        customer_da = DataAccess(CustomerInformation)
        return customer_da.find_by(CustomerInformation.family == family)


