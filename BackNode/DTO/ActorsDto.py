class Actors: 

    def __init__ (self, actor_id, last_name,  first_name):

        self.actor_id = actor_id
        self.last_name = last_name
        self.first_name = first_name

    #actor_id

    @property
    def actor_id(self):
        return self.actor_id 
    
    @actor_id.setter    
    def actor_id(self, actor_id):
        self.actor_id = actor_id

    #last_name

    @property
    def last_name(self):
        return self.last_name 
    
    @last_name.setter    
    def last_name(self, last_name):
        self.last_name = last_name

    #first_name

    @property
    def first_name(self):
        return self.first_name 
    
    @first_name.setter    
    def first_name(self, first_name):
        self.first_name = first_name