if __package__ is None: # ipython
    from app import db
else:                   # python app.py
    from ..app import db

all = ["roommates", "purchases", "ledgers"]
