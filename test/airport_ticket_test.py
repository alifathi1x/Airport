
from model.da.da import DataAccess
from model.entity.ticket_information import *

ticket = TicketInformation(2,2)
ticket_da = DataAccess(TicketInformation)
ticket_da.save(ticket)

print(ticket)