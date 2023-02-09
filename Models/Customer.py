from config import db
from flask import request, jsonify
from app import app 

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name  =  db.Column(db.String(155), nullable = False)
    deliveryAddress  =  db.Column(db.String(155), nullable = False)
    contact  =  db.Column(db.String(155), nullable = False)
    active  =  db.Column(db.Integer, nullable = False)


"""
@app.route('/the/add', methods=['POST'])
def add():
    try:
        json = request.json
        name = json["name"]
        deliveryAddress = json["deliveryAddress"]
        contact = json["contact"]
        active = json["active"]

        if name and deliveryAddress and contact and active and request.method == 'POST':
            client = Customer.Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)
            db.session.add(client)
            db.session.commit()
            resulat = jsonify('Customer a été bien enregister')
            return resulat
    except Exception as e:
        print(e)
        resulat = {"message":"Nous avons rencontré un problème"}
        return jsonify(resulat) """