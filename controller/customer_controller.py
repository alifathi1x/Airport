from model.entity.customer_information import CustomerInformation
from model.service.customer_service import CustomerService
from model.tools.logger import Logger

class CustomerController:
    @staticmethod
    def save(name, family, birth_date, national_id, passport_number):
        try:
            customer = CustomerInformation("ali","fathi","","aaa",1111111,)
            CustomerService.save(customer)
            Logger.info(f"customer Saved - {customer}")
            return True, customer
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(id,name, family, birth_date, national_id, passport_number):
        try:
            customer = CustomerInformation("ali","fathi","","a77777",2222222)
            customer.id = id
            CustomerService.edit(customer)
            Logger.info(f"customer Edited - {customer}")
            return True, customer
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            customer = CustomerService.remove(id)
            Logger.info(f"customer ID Removed - {customer}")
            return True, customer
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(name):
        try:
            customer = CustomerService.remove(name)
            Logger.info(f"customer removed - {customer}")
            return True, customer
        except Exception as e:
            Logger.info(f"{e}")
            return False, f"{e}"




    @staticmethod
    def findAll():
        try:
            customer_list = CustomerService.find_all()
            Logger.info(f"customer findAll()")
            return True, customer_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"


    @staticmethod
    def find_by_name(name):
        try:
            customer = CustomerService.find_by_name(name)
            Logger.info(f"customer find by name - {customer}")
            return True, customer
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_family(family):
        try:
            customer = CustomerService.find_by_family(family)
            Logger.info(f"customer find by family - {customer}")
            return True, customer
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"



