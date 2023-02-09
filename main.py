from app import app
from config import db
#from Models import Credit,Customer,Item,Order,OrderDetail,OrderStatus,Payment
from models import Customer,OrderDetail,Order,OrderStatus,Item
from flask import request,jsonify

with app.app_context():
    db.create_all()


################-----------------------------|FONCTIONS AJOUTER|----------------------------#########################
################-----------------------------|FONCTIONS AJOUTER|----------------------------#########################
################-----------------------------|FONCTIONS AJOUTER|----------------------------#########################
################-----------------------------|FONCTIONS AJOUTER|----------------------------#########################
@app.route('//add', methods=['POST'])
def add_customer():
    try:
        json = request.json
        name = json["name"]
        deliveryAddress = json["deliveryAddress"]
        contact = json["contact"]
        active = json["active"]

        if name and deliveryAddress and contact and active and request.method == 'POST':
            client = Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)
            db.session.add(client)
            db.session.commit()
            resulat = jsonify('Customer a été bien enregister')
            return resulat
    except Exception as e:
        print(e)
        resulat = {"message":"Nous avons rencontré un problème"}
        return jsonify(resulat) 
@app.route('/item/add', methods=['POST'])
def add_item():
    try:
        json = request.json
        weight = json["weight"]
        description = json["description"]

        if weight and description and request.method == 'POST':
            client = Item(weight = weight, description = description)
            db.session.add(client)
            db.session.commit()
            resulat = jsonify('Customer a été bien enregister')
            return resulat
    except Exception as e:
        print(e)
        resulat = {"message":"Nous avons rencontré un problème"}
        return jsonify(resulat) 

@app.route('/order/add', methods=['POST'])
def add_order():
    try:
        json = request.json
        createDate = json["createDate"]
        if  createDate and request.method == 'POST':
            client = Order(createDate= createDate)
            db.session.add(client)
            db.session.commit()
            resulat = jsonify('Customer a été bien enregister')
            return resulat
    except Exception as e:
        print(e)
        resulat = {"message":"Nous avons rencontré un problème"}
        return jsonify(resulat) 
@app.route('/orderDetail/add', methods=['POST'])
def add_orderDetail():
    try:
        json = request.json
        qty = json["qty"]
        taxStatus = json["taxStatus"]
        

        if qty and taxStatus and request.method == 'POST':
            client = OrderDetail(qty = qty , taxStatus = taxStatus)
            db.session.add(client)
            db.session.commit()
            resulat = jsonify('Customer a été bien enregister')
            return resulat

    except Exception as e:
        print(e)
        resulat = {"message":"Nous avons rencontré un problème"}
        return jsonify(resulat) 
"""
@app.route('/Payement/add', methods=['POST'])
def add_orderDetail():
    try:
        json = request.json
        amount = json["amount"]
        payment_mode = json["payment_mode"]
        

        if amount and payment_mode and request.method == 'POST':
            client = Payment(amamount =amount , payment_mode = payment_mode)
            db.session.add(client)
            db.session.commit()
            resulat = jsonify('Customer a été bien enregister')
            return resulat

    except Exception as e:
        print(e)
        resulat = {"message":"Nous avons rencontré un problème"}
        return jsonify(resulat) 

@app.route('/credit/add', methods=['POST'])
def add_credit():
    try:
        json = request.json
        number= json["number"]
        type = json["type"]
        expireDate = json["expireDate"]
        

        if number and type and expireDate and request.method == 'POST':
            credits = Credit(number = number, type = type, expireDate = expireDate)
            db.session.add(credits)
            db.session.commit()
            resulat = jsonify('Customer a été bien enregister')
            return resulat

    except Exception as e:
        print(e)
        resulat = {"message":"Nous avons rencontré un problème"}
        return jsonify(resulat) 

"""

@app.route('/customers', methods = ['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        data = [{"id":customers.id, "name":customers.name, "deliveryAddress":customers.deliveryAddress, "contact":customers.contact, "active":customers.active} for customers in customers]

        resultat = jsonify({"status_code":200, "Customer" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


if(__name__ == '__main__'):
    app.run()