from app import app
from config import db
#from Models import Cash,Check,Credit,Customer,Item,Order,OrderDetail,OrderStatus,Payment,WireTransfer
from Models.Customer import Customer
from Models.Credit import Credit
from Models.Cash import Cash
from Models.Check import Check
from Models.Item import Item
from Models.Order import Order
from Models.WireTransfer import WireTransfer
from Models.Payment import Payment
from Models.OrderDetail import OrderDetail
from Models.OrderStatus import OrderStatus
from flask import request,jsonify

with app.app_context():
    db.drop_all()
    db.create_all()


################-----------------------------|FONCTIONS AJOUTER|----------------------------#########################
################-----------------------------|FONCTIONS AJOUTER|----------------------------#########################
################-----------------------------|FONCTIONS AJOUTER|----------------------------#########################
################-----------------------------|FONCTIONS AJOUTER|----------------------------#########################

@app.route('/customer/add', methods = ['POST'])
def customer_add():
    try:
        json = request.json
        name = json['name']
        deliveryAddress = json['deliveryAddress']
        contact = json['contact']
        active = json['active']
        if name and deliveryAddress and contact and active and request.method == 'POST':     
            customer = Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)
            db.session.add(customer)
            db.session.commit()
            resultat = jsonify('Customer add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/order/add', methods = ['POST'])
def order_add():
    try:
        json = request.json
        print(json)
        createDate = json['createDate']
        customerId = json['customerId']
        if createDate and request.method == 'POST':
            orders = Order(createDate = createDate)
            if customerId :
                customer = Customer.query.filter_by(id = customerId).first()
                print(customer)
                orders.customer = customer
            db.session.add(orders)
            db.session.commit()
            resultat = jsonify('Order add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/orderStatus/add', methods = ['POST'])
def orderstatus_add():
    try:
        json = request.json
        CREATE = json['CREATE']
        SHIPPING = json['SHIPPING']
        DELIVERED = json['DELIVERED']
        PAID = json['PAID']

        if CREATE and SHIPPING and DELIVERED and PAID and request.method == 'POST':
            orderStatus = OrderStatus(CREATE = CREATE, SHIPPING = SHIPPING, DELIVERED = DELIVERED, PAID = PAID)
            db.session.add(orderStatus)
            db.session.commit()
            resultat = jsonify('Order Status add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/orderDetail/add', methods = ['POST'])
def orderdetail_add():
    try:
        json = request.json
        qty = json['qty']
        taxStatus = json['taxStatus']
        if qty and taxStatus and request.method == 'POST':
            orderDetail = OrderDetail(qty = qty, taxStatus = taxStatus)
            db.session.add(orderDetail)
            db.session.commit()
            resultat = jsonify('New Order Detail add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/item/add', methods = ['POST'])
def item_add():
    try:
        json = request.json
        weight = json['weight']
        description = json['description']
        if weight and description and request.method == 'POST':
            item = Item(weight = weight, description = description)
            db.session.add(item)
            db.session.commit()
            resultat = jsonify('New Item add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/payment/add', methods = ['POST'])
def payment_add():
    try:
        json = request.json
        amount = json['amount']
        if amount and request.method == 'POST':
            payments = Payment(amount = amount)
            db.session.add(payments)
            db.session.commit()
            resultat = jsonify('New Payment add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/credit/add', methods = ['POST'])
def credit_add():
    try:
        json = request.json
        number = json['number']
        type = json['type']
        expireDate = json['expireDate']
        if number and type and expireDate and request.method == 'POST':
            credits = Credit(number = number, type = type, expireDate = expireDate)
            db.session.add(credits)
            db.session.commit()
            resultat = jsonify('New Credit add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/Cash/add', methods = ['POST'])
def cash_add():
    try:
        json = request.json
        cashTendered = json['cashTendered']
        if cashTendered and request.method == 'POST':
            cashs = Cash(cashTendered = cashTendered)
            db.session.add(cashs)
            db.session.commit()
            resultat = jsonify('New Cash add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/check/add', methods = ['POST'])
def check_add():
    try:
        json = request.json
        name = json['name']
        bankID = json['bankID']
        if name and bankID and request.method == 'POST':
            checks = Check(name = name, bankID = bankID)
            db.session.add(checks)
            db.session.commit()
            resultat = jsonify('New Check add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/wiretransfer/add', methods = ['POST'])
def wiretransfer_add():
    try:
        json = request.json
        bankID = json['bankID']
        bankName = json['bankName']

        if bankID and bankName and request.method == 'POST':
            wiretransfer = WireTransfer(bankID = bankID, bankName = bankName)
            db.session.add(wiretransfer)
            db.session.commit()
            resultat = jsonify('New Wire Transfer add')
            return resultat
    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()




################-----------------------------|FONCTIONS GET|----------------------------#########################
################-----------------------------|FONCTIONS GET|----------------------------#########################
################-----------------------------|FONCTIONS GET|----------------------------#########################
################-----------------------------|FONCTIONS GET|----------------------------#########################








@app.route('/customers', methods = ['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        data = [{"id":customer.id, "name":customer.name, "deliveryAddress":customer.deliveryAddress, "contact":customer.contact, "active":customer.active} for customer in customers]

        resultat = jsonify({"status_code":200, "Customer" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()







@app.route('/order', methods = ['GET'])
def get_order():
    try:
        orders = Order.query.all()
        data = [{"id":order.id, "createData":order.createData} for order in orders]

        resultat = jsonify({"status_code":200, "Orders" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()







@app.route('/items', methods = ['GET'])
def get_items():
    try:
        items = Item.query.all()
        data = [{"id":item.id, "weight":item.weight, "description":item.description} for item in items]

        resultat = jsonify({"status_code":200, "Item" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()







@app.route('/orderDetail', methods = ['GET'])
def orderDetail():
    try:
        orderDetails = OrderDetail.query.all()
        data = [{"id":orderDetail.id, "qty":orderDetail.qty, "taxStatus":orderDetail.taxStatus} for orderDetail in orderDetails]
        resultat = jsonify({"status_code":200, "OrderDetail" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()







@app.route('/payement', methods = ['GET'])
def get_payement():
    try:
        payements = Payment.query.all()
        data = [{"id":payement.id, "name":payement.name} for payement in payements]

        resultat = jsonify({"status_code":200, "Payement" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()







@app.route('/credit', methods = ['GET'])
def get_credit():
    try:
        credits = Customer.query.all()
        data = [{"id":credit.id, "number":credit.number, "type":credit.type, "expireDate":credit.expireDate} for credit in credits]

        resultat = jsonify({"status_code":200, "credit" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/cash', methods = ['GET'])
def get_cash():
    try:
        cashs = Customer.query.all()
        data = [{"id":cash.id, "number":cash.cashTendered} for cash in cashs]

        resultat = jsonify({"status_code":200, "cash" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()







@app.route('/check', methods = ['GET'])
def get_check():
    try:
        check = Customer.query.all()
        data = [{"id":check.id, "name":check.name, "bandID":check.bandID} for check in check]

        resultat = jsonify({"status_code":200, "Check" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


if(__name__ =='__main__'):
    app.run()