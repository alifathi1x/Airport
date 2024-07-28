from model.entity.customer_information import CustomerInformation
from model.service.customer_service import CustomerService
from model.tools.decorator import exception_handling
class CustomerController:
    @classmethod
    @exception_handling
    def save(cls,name,family,birth_date,national_id,passport_number):
        customer = CustomerInformation(name,family,national_id,passport_number,birth_date)
        return True, CustomerService.save(customer)

    @classmethod
    @exception_handling
    def edit(cls,name,family,birth_date,national_id,passport_number):
        customer = CustomerInformation(name,family,national_id,passport_number,birth_date)
        customer.id = id
        return True, CustomerService.edit(customer)

    @classmethod
    @exception_handling
    def remove(cls,name,family,birth_date,national_id,passport_number):
        customer = CustomerInformation(name,family,national_id,passport_number,birth_date)
        return True, CustomerService.remove(customer)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, CustomerService.find_all()


    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        return True, CustomerService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_name(cls,name):
        return True, CustomerService.find_by_name(name)

    @classmethod
    @exception_handling
    def find_by_family(cls,family):
        return True, CustomerService.find_by_family(family)

