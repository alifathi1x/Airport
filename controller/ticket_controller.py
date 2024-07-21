from model.entity.ticket_information import TicketInformation
from model.service.ticket_service import TicketService
from model.tools.decorator import exception_handling

class TicketController:
    @classmethod
    @exception_handling
    def save(cls,seat_number, price):
        ticket = TicketInformation(seat_number, price)
        return True, TicketService.save(ticket)

    @classmethod
    @exception_handling
    def edit(cls,id,seat_number, price):
        ticket = TicketInformation(seat_number,price)
        ticket.id = id
        return True, TicketService.edit(ticket)

    @classmethod
    @exception_handling
    def remove(cls,id):
        return True, TicketService.remove(id)


    @classmethod
    @exception_handling
    def find_all(cls):
        return True, TicketService.find_all()



    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        return True, TicketService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_seat_number(cls,seat_number):
        return True, TicketService.find_by_seat_number(seat_number)

