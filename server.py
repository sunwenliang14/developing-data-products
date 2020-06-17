from random import randint
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/roll-dice')
def roll_dice():
    roll = randint(1, 6)
    return f'You rolled a {roll}'


@app.route('/order-pizza')
def show_order_pizza_form():
    return render_template('order-pizza-form.html')


@app.route('/order-pizza', methods=['POST'])
def handle_pizza_order_submission():

    topping1 = request.form['topping1']
    topping2 = request.form['topping2']
    pizza = f'{topping1} and {topping2}'

    return f'One pizza with {pizza} on the way!

@app.route("/is-spam")
def spam_form():
    return render_template("spam-input-form.html")

@app.route('/spam-ham-result', methods=['POST'])
def spam_ham_prediction():
    message = request.form['message']
    result = predict(message)
    return render_template('spam-ham-result.html', message=message, result=result)