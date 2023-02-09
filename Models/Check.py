from config import db
from Models.Payment import Payment

class Check (Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    name = db.Column(db.String(120), nullable = False)
    bankID = db.Column(db.String(120), nullable = False)
    
    __mapper_args__ = {
        'polymorphic_identity' : 'Check'
    }
