from model.entity.customer_information import CustomerInformation
from model.entity.fly_information import FlyInformation


class TicketInformation(FlyInformation,CustomerInformation):
    def __init__(self,id,seat_number,price):
        self.id = None
        self.seat_number = seat_number
        self.price = price

    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_seat_number(self):
        return self._seat_number
    def set_seat_number(self,seat_number):
        if isinstance(seat_number,int):
            self._seat_number = seat_number
        else:
            raise ValueError("Invalid seat number")

    def get_price(self):
        return self._price
    def set_price(self,price):
        if isinstance(price,int):
            self._price = price
        else:
            raise ValueError("Invalid price")

    seat_number = property(get_seat_number,set_seat_number)
    price = property(get_price,set_price)