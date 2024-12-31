from flask import Flask
from models import db, init_app
app = Flask(__name__)

init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome to the Referral System!"


if __name__ == "__main__":
    app.run(debug=True)
