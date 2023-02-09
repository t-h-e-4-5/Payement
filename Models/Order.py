from config import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    createDate = db.Column(db.Date, nullable = False)
    ### Les relations 
    #### OneToMany
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = True)
    customer = db.relationship('Customer', foreign_keys = [customerId])