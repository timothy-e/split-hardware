from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dataRoommate import Roommate, Purchase, House


app = Flask(__name__)

Evan = Roommate("Evan")
Tristan = Roommate("Tristan")
Tim = Roommate("Tim")
Emmy = Roommate("Emmy")

home = House("R204")
home.add_member(Evan)
home.add_member(Tim)
home.add_member(Tristan)
home.add_member(Emmy)


@app.route("/", methods=["GET"])
def overview():
    max_i = max(len(member.purchases) for member in home.members)
    return render_template("overview.html", home=home, limit = max_i)


@app.route("/add_purchase/", methods=["POST"])  # pass in params by cURL: name, cost, item
def add_purchase():
    name = request.args.get("name")
    cost = request.args.get("cost")
    item = request.args.get("item")
    # add a purchase to the Roommate with name=name

    for member in home.members:
        if member.name == name:
            currentRoommate = member

    item = Purchase(item, float(cost))
    currentRoommate.add_item(item)
    return item.as_json()


@app.route("/settle_debts/", methods=["POST"])
def settle_debts():
    # reset all balances to 0
    for member in home.members:
        member.set_to_zero()
    return home.as_json()


@app.route("/get_balance/<identity>", methods=["GET"])
def get_balance(identity):
    return render_template("debt.html", home=home, identity=identity)



if __name__ == "__main__":
    app.run(debug=True)
