from view.table import Table
from model.da.da import DataAccess
from model.entity.customer_information import CustomerInformation
from controller.customer_controller import CustomerController
from model.service.customer_service import CustomerService
from view.label_text import TextWithLabel
from tkinter import *

class CustomerView:
    def customer_table_click(self,row):
        CustomerInformation = self.customer_da.find_by_id(int(row[0]))
        print(CustomerInformation)

    def remove(self,name,family,birth_date,national_id,passport_number):
        customer = CustomerInformation(name,family,birth_date,national_id,passport_number)
        CustomerController.remove(customer)
        #to do: balad nistam

    def save(self):
        customer = CustomerService.remove(CustomerInformation)
        #to do: balad nistam



    def __init__(self):
        self.customer_da = DataAccess(CustomerInformation)

        self.win = Tk()
        self.win.title("Customer View")
        self.win.geometry("1000x1000")
        self.customer_table = Table(self.win,["id","name","family","birth_date","national_id","passport_number"],
                                [20,100,100,100,100,100,100,100],300, 100,
                                    self.customer_table_click)

        self.total = TextWithLabel(self.win,"name",20,20)
        self.total = TextWithLabel(self.win,"family",20,50)
        self.total = TextWithLabel(self.win,"birth_date",20,80)
        self.total = TextWithLabel(self.win,"national_id",20,110)
        self.total = TextWithLabel(self.win,"passport",20,140)
        self.button = Button(self.win,text="Delete",command=self.remove).place(x=200,y=200)
        self.button = Button(self.win,text="save",command=self.save).place(x=160,y=200)
        self.win.bind()
        self.win.mainloop()


