from flask import Flask, Response, render_template, jsonify, request

app = Flask(__name__)

bus_customer = []
total_no_bus_tickets1 = [{"total_ticket": 10}]


train_customer = []
total_no_train_tickets1 = [{"total_ticket": 20}]


flight_customer = []
total_no_flight_tickets1 = [{"total_ticket": 30}]

# -------------------BUS----------------------------------------


@app.route('/bus/user/', methods=['GET'])
def get_all_user():
    return jsonify({'user': bus_customer})


@app.route('/bus/user/<string:name>/', methods=['GET'])
def get_one_user(name):
    for i in range(len(bus_customer)):
        if bus_customer[i]['name'] == name:
            return jsonify({'user': bus_customer[i]})
    return jsonify({'message': "there is no user here"})


@app.route('/bus/book/', methods=['POST'])
def bus_booking():
    ticket = int(request.form.get('no_of_tickets'))
    user = {
        "name": request.form.get('name'),
        "age": request.form.get('age'),
        "gender": request.form.get('gender'),
        "startpoint": request.form.get('startpoint'),
        "destination": request.form.get('destination'),
        "tickets": ticket}
    if ticket >= total_no_bus_tickets1[0]['total_ticket']+1:
        return jsonify({"message": "Only"+" "+str(total_no_bus_tickets1)+" "+"tickets available now, please book again?"})
    else:
        booked_tickets = total_no_bus_tickets1[0]['total_ticket']-ticket
        total_no_bus_tickets1[0]['total_ticket'] = booked_tickets
        bus_customer.append(user)
        return jsonify({'user': user, "message": "tickets was booked"})


@app.route('/bus/cancel/<string:name>', methods=['POST'])
def user_bus_ticket_canceling(name):
    for i in range(len(bus_customer)):
        if name == bus_customer[i]['name']:
            p = request.form.get('no_of_tickets')
            if bus_customer[i]['tickets'] >= int(p):
                new = bus_customer[i]["tickets"]-int(p)
                cvo = int(p) + total_no_bus_tickets1[0]['total_ticket']
                total_no_bus_tickets1[0]['total_ticket'] = cvo
                bus_customer[i]['tickets'] = new
                return jsonify({'no of tickets canceled': p, 'message': "tickets was successfully canceled"})
            else:
                return jsonify({'bus_customer[i]': bus_customer[i]['tickets'], 'no of tickets': p, 'message': "but you are tring to cancel more than yours"})
        else:
            return jsonify({"message": "You were selected wrong option please selerct currect one:"})


@app.route('/bus/show_avai', methods=['GET'])
def show_avail_in_bus():
    return jsonify({
        "message": "Now"+" "+str(total_no_bus_tickets1[0]['total_ticket'])+" "+"are available"})


@app.route('/bus/show_booking', methods=['GET'])
def user_show_booking_in_bus():
    if len(bus_customer) == 0:
        return jsonify({"message": "there is no booking here!!"})
    else:
        for i in range(len(bus_customer)):
            return jsonify({"message1": "hi"+" "+str(bus_customer[i]['name'])+" " + "you booked"+" " + str(bus_customer[i]['tickets'])+"_"+"tickets"})


# -------------------------TRAIN-------------------------------
@app.route('/train/user/', methods=['GET'])
def get_all_user():
    return jsonify({'user': train_customer})


@app.route('/train/user/<string:name>/', methods=['GET'])
def get_one_user(name):
    for i in range(len(train_customer)):
        if train_customer[i]['name'] == name:
            return jsonify({'user': train_customer[i]})
    return jsonify({'message': "there is no user here"})


@app.route('/train/book/', methods=['POST'])
def bus_booking():
    ticket = int(request.form.get('no_of_tickets'))
    user = {
        "name": request.form.get('name'),
        "age": request.form.get('age'),
        "gender": request.form.get('gender'),
        "startpoint": request.form.get('startpoint'),
        "destination": request.form.get('destination'),
        "tickets": ticket}
    if ticket >= total_no_train_tickets1[0]['total_ticket']+1:
        return jsonify({"message": "Only"+" "+str(total_no_train_tickets1)+" "+"tickets available now, please book again?"})
    else:
        booked_tickets = total_no_train_tickets1[0]['total_ticket']-ticket
        total_no_train_tickets1[0]['total_ticket'] = booked_tickets
        train_customer.append(user)
        return jsonify({'user': user, "message": "tickets was booked"})


@app.route('/train/cancel/<string:name>', methods=['POST'])
def user_bus_ticket_canceling(name):
    for i in range(len(train_customer)):
        if name == train_customer[i]['name']:
            p = request.form.get('no_of_tickets')
            if train_customer[i]['tickets'] >= int(p):
                new = train_customer[i]["tickets"]-int(p)
                cvo = int(p) + total_no_train_tickets1[0]['total_ticket']
                total_no_train_tickets1[0]['total_ticket'] = cvo
                train_customer[i]['tickets'] = new
                return jsonify({'no of tickets canceled': p, 'message': "tickets was successfully canceled"})
            else:
                return jsonify({'bus_customer[i]': train_customer[i]['tickets'], 'no of tickets': p, 'message': "but you are tring to cancel more than yours"})
        else:
            return jsonify({"message": "You were selected wrong option please selerct currect one:"})


@app.route('/train/show_avai', methods=['GET'])
def show_avail_in_bus():
    return jsonify({
        "message": "Now"+" "+str(total_no_train_tickets1[0]['total_ticket'])+" "+"are available"})


@app.route('/train/show_booking', methods=['GET'])
def user_show_booking_in_bus():
    if len(train_customer) == 0:
        return jsonify({"message": "there is no booking here!!"})
    else:
        for i in range(len(bus_customer)):
            return jsonify({"message1": "hi"+" "+str(train_customer[i]['name'])+" " + "you booked"+" " + str(train_customer[i]['tickets'])+"_"+"tickets"})


# ---------------------------FLIGHT---------------------------------
@app.route('/flight/user/', methods=['GET'])
def get_all_user():
    return jsonify({'user': bus_customer})


@app.route('/flight/user/<string:name>/', methods=['GET'])
def get_one_user(name):
    for i in range(len(bus_customer)):
        if bus_customer[i]['name'] == name:
            return jsonify({'user': bus_customer[i]})
    return jsonify({'message': "there is no user here"})


@app.route('/flight/book/', methods=['POST'])
def bus_booking():
    ticket = int(request.form.get('no_of_tickets'))
    user = {
        "name": request.form.get('name'),
        "age": request.form.get('age'),
        "gender": request.form.get('gender'),
        "startpoint": request.form.get('startpoint'),
        "destination": request.form.get('destination'),
        "tickets": ticket}
    if ticket >= total_no_flight_tickets1[0]['total_ticket']+1:
        return jsonify({"message": "Only"+" "+str(total_no_flight_tickets1)+" "+"tickets available now, please book again?"})
    else:
        booked_tickets = total_no_flight_tickets1[0]['total_ticket']-ticket
        total_no_flight_tickets1[0]['total_ticket'] = booked_tickets
        flight_customer.append(user)
        return jsonify({'user': user, "message": "tickets was booked"})


@app.route('/flight/cancel/<string:name>', methods=['POST'])
def user_bus_ticket_canceling(name):
    for i in range(len(flight_customer)):
        if name == flight_customer[i]['name']:
            p = request.form.get('no_of_tickets')
            if flight_customer[i]['tickets'] >= int(p):
                new = flight_customer[i]["tickets"]-int(p)
                cvo = int(p) + total_no_flight_tickets1[0]['total_ticket']
                total_no_flight_tickets1[0]['total_ticket'] = cvo
                flight_customer[i]['tickets'] = new
                return jsonify({'no of tickets canceled': p, 'message': "tickets was successfully canceled"})
            else:
                return jsonify({'bus_customer[i]': flight_customer[i]['tickets'], 'no of tickets': p, 'message': "but you are tring to cancel more than yours"})
        else:
            return jsonify({"message": "You were selected wrong option please selerct currect one:"})


@app.route('/flight/show_avai', methods=['GET'])
def show_avail_in_bus():
    return jsonify({
        "message": "Now"+" "+str(total_no_flight_tickets1[0]['total_ticket'])+" "+"are available"})


@app.route('/flight/show_booking', methods=['GET'])
def user_show_booking_in_bus():
    if len(flight_customer) == 0:
        return jsonify({"message": "there is no booking here!!"})
    else:
        for i in range(len(flight_customer)):
            return jsonify({"message1": "hi"+" "+str(flight_customer[i]['name'])+" " + "you booked"+" " + str(flight_customer[i]['tickets'])+"_"+"tickets"})


if __name__ == '__main__':
    app.run(debug=True)
