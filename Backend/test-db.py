from extensions import db
from models import User, Referral
from flask import Flask

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    # Add 10 users
    users = [
        # User(name="Taslima Begum", email="taslima@example.com", password="securepassword", referral_code="REF12345", referrals_count=10),
        # User(name="John Doe", email="john.doe@example.com", password="anothersecurepassword", referral_code="REF67890", referrals_count=20),
        User(name="Alice Smith", email="alice.smith@example.com", password="alicepassword", referral_code="REF11223", referrals_count=5),
        User(name="Bob Johnson", email="bob.johnson@example.com", password="bobbypass", referral_code="REF33445", referrals_count=7),
        User(name="Charlie Brown", email="charlie.brown@example.com", password="charlie123", referral_code="REF55667", referrals_count=3),
        User(name="Daisy Hill", email="daisy.hill@example.com", password="daisypass", referral_code="REF77889", referrals_count=12),
        User(name="Evan Wright", email="evan.wright@example.com", password="evansecure", referral_code="REF99001", referrals_count=8),
        User(name="Fiona White", email="fiona.white@example.com", password="fionapass", referral_code="REF22334", referrals_count=6),
        User(name="George King", email="george.king@example.com", password="georgeking123", referral_code="REF44556", referrals_count=4),
        User(name="Hannah Lee", email="hannah.lee@example.com", password="hannahsecure", referral_code="REF66778", referrals_count=15)
    ]

    # Add users to the database
    db.session.add_all(users)
    db.session.commit()

    print("Users added successfully!")

    # Add referrals for some users
    referrals = [
        # Referral(referrer_id=users[0].id, referred_email="referred1@example.com"),
        # Referral(referrer_id=users[1].id, referred_email="referred2@example.com"),
        Referral(referrer_id=users[2].id, referred_email="referred3@example.com"),
        Referral(referrer_id=users[3].id, referred_email="referred4@example.com"),
        Referral(referrer_id=users[4].id, referred_email="referred5@example.com"),
        Referral(referrer_id=users[5].id, referred_email="referred6@example.com"),
        Referral(referrer_id=users[6].id, referred_email="referred7@example.com"),
        Referral(referrer_id=users[7].id, referred_email="referred8@example.com"),
        # Referral(referrer_id=users[8].id, referred_email="referred9@example.com"),
        Referral(referrer_id=users[9].id, referred_email="referred10@example.com")
    ]

    # Add referrals to the database
    db.session.add_all(referrals)
    db.session.commit()

    print("Referrals added successfully!")
