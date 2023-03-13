from . import db


class Properties(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True,  autoincrement =True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.Integer)
    description = db.Column(db.String(250))
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(128))
    price =  db.Column(db.Integer)
    type = db.Column(db.String(20))
    photo = db.Column(db.String(128))



    def __init__(self, title, description, bedrooms, bathrooms, location, price, type, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.description = description
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.photo = photo

  