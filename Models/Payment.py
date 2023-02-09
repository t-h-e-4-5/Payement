from config import db

class Paymhent(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    amount = db.Column(db.Float, nullable  = False)
    payment_mode = db.Column(db.String(121), nullable  = False)
    __mapper_args__ = { 'polymorohic_on':payment_mode}