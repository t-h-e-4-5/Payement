from config import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    amount = db.Column(db.Float, nullable  = False)
    payment_mode = db.Column(db.String(121), nullable  = False)
    
    ##### Liaison 
    #### OneToMany
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])
        ## Methode pour rendre la classe Mere(Heritage)
    
    __mapper_args__ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': payment_mode
    }
