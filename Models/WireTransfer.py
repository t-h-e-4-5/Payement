from config import db
from Models.Payment import Payment

class WireTransfer (Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    bankID = db.Column(db.String(120), nullable = False)
    bankName = db.Column(db.String(120), nullable = False)

    __mapper_args__ = {
        'polymorphic_identity' : 'wireTransfer'
    }
