from tkinter import *
from model.entity.fly_information import FlyInformation
from controller.fly_controller import FlyController
from model.da.da import DataAccess
from view.table import Table
from view.label_text import TextWithLabel


class FlyView:
    def fly_table_click(self, row):
        FlyInformation = self.fly_da.find_by_id(int(row[0]))
        print(FlyInformation)

    def remove(self):
        FlyController.remove(FlyInformation)
        #to do: balad nistam

    def save(self):
       FlyController.save(FlyInformation)
        #to do: balad nistam


    def __init__(self):
        self.fly_da = DataAccess(FlyInformation)
        self.win = Tk()
        self.win.title("Fly View")
        self.win.geometry("1000x1000")
        self.fly_table = Table(self.win,["fly_number","direction","destination","date_time","fly_type","status"]
                               ,[20,100,100,100,100,100,100,100],300,100,self.fly_table_click)

        self.total = TextWithLabel(self.win,"fly_number",20,20)
        self.total = TextWithLabel(self.win,"direction",20,50)
        self.total = TextWithLabel(self.win,"destination",20,80)
        self.total = TextWithLabel(self.win,"date_time",20,110)
        self.total = TextWithLabel(self.win,"fly_type",20,140)
        self.total = TextWithLabel(self.win,"status",20,170)
        self.button = Button(self.win,text="Delete",command=self.remove).place(x=200,y=200)
        self.button = Button(self.win,text="save",command=self.save).place(x=160,y=200)
        self.win.mainloop()