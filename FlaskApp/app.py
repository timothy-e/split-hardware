from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dataRoommate import *


app = Flask(__name__)

#########################################
#                                       #
#  define models here (python classes)  #
#                                       #
#########################################

Evan = Roommate("Evan")
Tristan = Roommate("Tristan")
Tim = Roommate("Tim")
Emmy = Roommate("Emmy")

home = House("R204")
home.add_member(Evan)
home.add_member(Tim)
home.add_member(Tristan)
home.add_member(Emmy)

@app.route("/")
def main():
    return render_template('index.html', id=None)

@app.route("/add_purchase/", methods=["POST"]) # pass in params by cURL: name, cost, item
def add_purchase():
    name = request.args.get('name')
    cost = request.args.get('cost')
    item = request.args.get('item')
    # add a purchase to the Roommate with name=name
    
    for member in house.members:
        if member.roommate == name:
            currentRoommate = member
        
    item = Purchase("item", cost)
    currentRoommate.add_item(item)
    pass


@app.route("/settle_debts/", methods=["POST"])
def settle_debts():
    # reset all balances to 0
    for member in house.members:
        member.set_to_zero()
    pass

@app.route("/get_balance/<identity>", methods=["GET"])
def get_balance(identity):

    return render_template('debt.html', home = home, identity = identity)
    # create a page with all debt info for Roommate with name=name
    # query for Roommate
    # pass into a render template
    pass

if __name__ == "__main__":
    app.run(debug=True)
