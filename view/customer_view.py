from view.table import Table
from model.da.da import DataAccess
from model.entity.customer_information import CustomerInformation
from view.label_text import TextWithLabel
from tkinter import *

class CustomerView:
    def customer_table_click(self,row):
        CustomerInformation = self.customer_da.find_by_id(int(row[0]))
        print(CustomerInformation)

    def __init__(self):
        self.customer_da = DataAccess(CustomerInformation)

        self.win = Tk()
        self.win.title("Customer View")
        self.win.geometry("1000x1000")
        self.customer_table = Table(self.win,["id","name","family","birth_date","national_id","passport_number"],
                                [20,100,100,100,100,100,100,100],300, 100,
                                    self.customer_table_click)

        self.total = TextWithLabel(self.win,"name",20,20)
        self.win.bind()
        self.win.mainloop()


