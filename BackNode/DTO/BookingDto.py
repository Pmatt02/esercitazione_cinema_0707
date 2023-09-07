class Booking:

    def __init__(self, first_name, last_name, n_tickets, screening_id):

        self.first_name = first_name
        self.last_name = last_name
        self.n_tickets = n_tickets
        self.screening_id = screening_id

    #first_name

    @property
    def first_name(self):
        return self.first_name 
    
    @first_name.setter    
    def first_name(self, first_name):
        self.first_name = first_name

    #last_name

    @property
    def last_name(self):
        return self.last_name 
    
    @last_name.setter    
    def last_name(self, last_name):
        self.last_name = last_name

    #n_tickets

    @property
    def n_tickets(self):
        return self.n_tickets 
    
    @n_tickets.setter    
    def n_tickets(self, n_tickets):
        self.n_tickets = n_tickets

    #screening_id

    @property
    def screening_id(self):
        return self.screening_id 
    
    @screening_id.setter    
    def screening_id(self, screening_id):
        self.screening_id = screening_id