class Film:

    def __init__(self, film_id, image, length, plot, rating, title, relase_date):

        self.film_id = film_id
        self.image = image
        self.length = length
        self.plot = plot
        self.rating = rating
        self.title = title
        self.relase_date = relase_date

    #film id

    @property
    def film_id(self):
        return self.film_id
    
    @film_id.setter
    def film_id(self, film_id):
        self.film_id = film_id

    #image

    @property
    def image(self):
        return self.image
    
    @image.setter
    def image(self, image):
        self.image = image

    #length

    @property
    def length(self):
        return self.length
    
    @length.setter
    def length(self, length):
        self.length = length

    #plot

    @property
    def plot(self):
        return self.plot
    
    @plot.setter
    def plot(self, plot):
        self.plot = plot

    #rating

    @property
    def rating(self):
        return self.rating
    
    @rating.setter
    def rating(self, rating):
        self.rating = rating

    #title

    @property
    def title(self):
        return self.title
    
    @title.setter
    def title(self, title):
        self.title = title

    #relase_date

    @property
    def relase_date(self):
        return self.relase_date
    
    @relase_date.setter
    def relase_date(self, relase_date):
        self.relase_date = relase_date