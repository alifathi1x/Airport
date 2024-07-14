from controller.exeptions import TicketNotFoundError
from model.da.da import DataAccess
from model.entity.ticket_information import TicketInformation

class TicketService:
    @staticmethod
    def save(ticket):
        ticket_da = DataAccess(TicketInformation)
        ticket_da.save(ticket)
        return ticket

    @staticmethod
    def edit(ticket):
        ticket_da = DataAccess(TicketInformation)
        if ticket_da.find_by_id(ticket.id):
            ticket_da.edit(ticket)
            return ticket
        else:
            raise TicketNotFoundError()

    @staticmethod
    def remove(ticket):
        ticket_da = DataAccess(TicketInformation)
        if ticket_da.find_by_id(ticket.id):
            return ticket_da.remove(ticket)
        else:
            raise TicketNotFoundError()

    @staticmethod
    def find_all():
        ticket_da = DataAccess(TicketInformation)
        return ticket_da.find_all()

    @staticmethod
    def find_by_id(id):
        ticket_da = DataAccess(TicketInformation)
        return ticket_da.find_by_id(id)

    @staticmethod
    def find_by_seat_number(seat_number):
        ticket_da = DataAccess(TicketInformation)
        return ticket_da.find_by(TicketInformation.seat_number == seat_number)


