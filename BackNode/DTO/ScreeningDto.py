class Screening:

    def __init__(self, screening_id, time, film_id, is_bookable):
        
        self.screening_id = screening_id
        self.time = time
        self.film_id = film_id
        self.is_bookable = is_bookable

    #screening_id

    @property
    def screening_id(self):
        return self.screening_id
    
    @screening_id.setter
    def screening_id(self, screening_id):
        self.screening_id = screening_id

    #time

    @property
    def time(self):
        return self.time
    
    @time.setter
    def time(self, time):
        self.time = time

    #film_id

    @property
    def film_id(self):
        return self.film_id
    
    @film_id.setter
    def film_id(self, film_id):
        self.film_id = film_id

    #is_bookable

    @property
    def is_bookable(self):
        return self.is_bookable
    
    @is_bookable.setter
    def is_bookable(self, is_bookable):
        self.is_bookable = is_bookable