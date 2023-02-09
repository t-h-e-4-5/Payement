from config import db

class Customer (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    deliveryAddress = db.Column(db.String(120), nullable = False)
    contact = db.Column(db.String(120), nullable = True)
    active = db.Column(db.Boolean, nullable = False)


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