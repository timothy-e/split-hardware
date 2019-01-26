from . import db

class Ledger(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    owed_id = db.Column(db.String(120), ForeignKey('Roommate.id'))
    owing_id = db.Column(db.String(120), ForeignKey('Roommate.id'))
    amount = db.Column(db.Integer)
