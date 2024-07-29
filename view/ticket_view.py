from tkinter import *
import tkinter.messagebox as msg
from model.entity.ticket_information import TicketInformation
from model.da.da import DataAccess
from controller.ticket_controller import TicketController
from view.table import Table
from view.label_text import TextWithLabel

class TicketView:
    def ticket_table_click(self,row):
        TicketInformation = self.ticket_da.find_by_id(int(row[0]))
        print(TicketInformation)

    def remove(self):
        TicketController.remove(TicketInformation)
        msg.showinfo("remove",f"Ticket has been removed")

    def save(self):
        status, result = TicketController.save(TicketInformation)
        if status:
            msg.showinfo("save", f"Ticket has been saved {result}")
        else:
            msg.showinfo("Error", f"Ticket could not be saved {result}")






    def __init__(self):
        self.ticket_da = DataAccess(TicketInformation)
        self.win = Tk()
        self.win.title("Ticket_View")
        self.win.geometry("1000x1000")
        self.ticket_table = Table(self.win,["seat_number","price"],[100,100],300,100,self.ticket_table_click)
        self.total = TextWithLabel(self.win,"seat_number",20,20)
        self.total = TextWithLabel(self.win,"price",20,50)
        self.button = Button(self.win,text="save").place(x=200,y=200)
        self.button = Button(self.win,text="delete").place(x=150,y=200)
        self.win.mainloop()


