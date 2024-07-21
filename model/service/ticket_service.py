from controller.exeptions import TicketNotFoundError
from model.da.da import DataAccess
from model.entity.ticket_information import TicketInformation
from model.tools.decorator import *

class TicketService:
    @classmethod
    def save(cls,ticket):
        ticket_da = DataAccess(TicketInformation)
        ticket_da.save(ticket)
        return ticket

    @classmethod
    def edit(cls,ticket):
        ticket_da = DataAccess(TicketInformation)
        if ticket_da.find_by_id(ticket.id):
            ticket_da.edit(ticket)
            return ticket
        else:
            raise TicketNotFoundError()

    @classmethod
    def remove(cls,ticket):
        ticket_da = DataAccess(TicketInformation)
        if ticket_da.find_by_id(id):
            return ticket_da.remove(ticket)
        else:
            raise TicketNotFoundError()

    @classmethod
    def find_all(cls):
        ticket_da = DataAccess(TicketInformation)
        return ticket_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        ticket_da = DataAccess(TicketInformation)
        return ticket_da.find_by_id(id)

    def find_by_seat_number(self, seat_number):
        ticket_da = DataAccess(TicketInformation)
        return ticket_da.find_by(seat_number.seat_number == seat_number.seat_number)