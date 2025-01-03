from flask import Blueprint, request, jsonify, render_template
from extensions import db, cache
from models import User, Referral
from referral.utils import increment_referrals_count

referral_bp = Blueprint('referral', __name__)

@referral_bp.route('/process_referral', methods=['POST'])
def process_referral():
    """Handles new user signup through a referral link."""
    referred_email = request.form.get('email')
    referrer_code = request.form.get('referrer_code')

    # Validate input
    if not referred_email or not referrer_code:
        return jsonify({'error': 'Email and referrer code are required'}), 400

    # Find the referrer
    referrer = User.query.filter_by(referral_code=referrer_code).first()
    if not referrer:
        return jsonify({'error': 'Invalid referrer code'}), 404

    # Add a referral record
    referral = Referral(referrer_id=referrer.id, referred_email=referred_email)
    db.session.add(referral)
    db.session.commit()

    # Increment the referrer’s referral count
    increment_referrals_count(referrer.id)

    return jsonify({'message': 'Referral processed successfully'})


@referral_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """Fetches and returns the leaderboard data as JSON."""
    # Fetch top 7 users by referrals_count in descending order
    users = User.query.order_by(User.referrals_count.desc()).limit(7).all()

    # Format the leaderboard data
    leaderboard = [
        {
            "rank": index + 1,
            "name": user.name,
            "profilePicture": user.profile_picture,
            "score": user.referrals_count
        }
        for index, user in enumerate(users)
    ]
    return jsonify(leaderboard)
