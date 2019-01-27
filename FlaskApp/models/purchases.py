from . import db

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    item_name = db.Column(db.String(120))
    cost = db.Column(db.Float)
    buyer_id = db.Column(db.ForeignKey('Roommate.id'))
