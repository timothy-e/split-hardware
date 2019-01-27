from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

#########################################
#                                       #
#  define models here (python classes)  #
#                                       #
#########################################

@app.route("/")
def main():
    return render_template('index.html', id=None)

@app.route("/add_purchase/", methods=["POST"]) # pass in params by cURL: name, cost, item
def add_purchase():
    name = request.args.get('name')
    cost = request.args.get('cost')
    item = request.args.get('item')
    # add a purchase to the Roommate with name=name
    pass


@app.route("/settle_debts/", methods=["POST"])
def settle_debts():
    # reset all balances to 0
    pass

@app.route("/get_balance/<name>", methods=["GET"])
def get_balance(name):
    # create a page with all debt info for Roommate with name=name
    # query for Roommate
    # pass into a render template
    pass

if __name__ == "__main__":
    app.run(debug=True)
