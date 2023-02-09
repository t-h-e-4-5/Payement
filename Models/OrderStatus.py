import enum
from sqlalchemy import Enum
from config import db

class OrderStatus (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    CREATE = db.Column(db.Integer, nullable = False)
    SHIPPING = db.Column(db.Integer, nullable = False)
    DELIVERED = db.Column(db.Integer, nullable = False)
    PAID = db.Column(db.Integer, nullable = False)


"""
class OrderStatus(enum.Enum):
    CREATE = 0
    SHIPPING = 1
    DELIVERED = 2
    PAID = 3
"""