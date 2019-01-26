from . import db

class Roommate(db.Model):
    # id (pk)
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    purchases = db.relationship('Purchase')
    payments = db.relationship('Ledger')
    owing = db.relationship('Ledger')
