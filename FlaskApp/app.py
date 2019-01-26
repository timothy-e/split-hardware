from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def main():
    return render_template('index.html', id=None)

@app.route("/<id>")
def page_with_id(id):
    return render_template('index.html', id=id)

if __name__ == "__main__":
    app.run(debug=True)
