import random
import string
from extensions import db
from models import User

def generate_referral_code(length=8):
    """Generates a unique referral code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def increment_referrals_count(referrer_id):
    """Increments the referrals count for the specified user."""
    referrer = User.query.filter_by(id=referrer_id).first()
    if referrer:
        referrer.referrals_count += 1
        db.session.commit()
