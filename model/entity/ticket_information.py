from model.entity.customer_information import CustomerInformation
from model.entity.fly_information import FlyInformation


class TicketInformation(FlyInformation,CustomerInformation):
    def __init__(self,id,seat_number,price):
        self.id = None
        self.seat_number = seat_number
        self.price = price