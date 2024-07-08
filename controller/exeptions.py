
class FlyNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("Fly not found")

class CustomerNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("Customer not found")

class TicketNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("Ticket not found")
