from config import db
import enum
from sqlalchemy import Enum
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name  =  db.Column(db.String(155), nullable = False)
    deliveryAddress  =  db.Column(db.String(155), nullable = False)
    contact  =  db.Column(db.String(155), nullable = False)
    active  =  db.Column(db.Boolean, nullable = False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    weight = db.Column(db.Float, nullable = False)  
    description = db.Column(db.String(155), nullable = False)
      

class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    qty = db.Column(db.Integer, nullable = False)  
    taxStatus = db.Column(db.String(155), nullable = False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    createDate = db.Column(db.Date, nullable = False)

class OrderStatus(enum.Enum):
    CREATE = 0
    SHIPPING = 1
    DELIVERED = 2
    PAID = 3
#t = Table('data', MetaData(),Column('value'),Enum(OrderStatus))

"""
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    amount = db.Column(db.Float, nullable  = False)
    payment_mode = db.Column(db.String(121), nullable  = False)
    __mapper_args__ = { 'polymorohic_on':payment_mode}

class Credit(Payment):
    id = db.Column(db.Integer, primary_key = True , nullable = False )
    number  = db.Column(db.Float, nullable = False )
    type = db.Column(db.String(122),nullable = True)
    expireDate  = db.Column
    __mapper_args__ = { 'polymorohic_identity':"Credit"}

"""