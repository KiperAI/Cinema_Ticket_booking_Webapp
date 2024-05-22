from flask import Flask, request, render_template, redirect, url_for
from main import User, Seat, Card, Ticket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy_ticket', methods=['POST'])
def buy_ticket():
    name = request.form['name']
    seat_id = request.form['seat_id']
    card_type = request.form['card_type']
    card_number = request.form['card_number']
    card_cvc = request.form['card_cvc']
    card_holder = request.form['card_holder']

    user = User(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

    message = user.buy(seat=seat, card=card)
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)