from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User,Referral
from referral.utils import generate_referral_code

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        referral_code = request.form.get('referral_code', None)  # Optional

        # Validate input
        if not name or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Check if the user already exists
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already registered'}), 400

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Generate a unique referral code
        new_referral_code = generate_referral_code()

        # Handle referral logic
        if referral_code:
            referrer = User.query.filter_by(referral_code=referral_code).first()
            if referrer:
                # Add a referral record
                referral = Referral(referrer_id=referrer.id, referred_email=email)
                db.session.add(referral)

                # Increment referrer's referral count
                referrer.referrals_count += 1

        # Save the new user
        user = User(
            name=name,
            email=email,
            password=hashed_password,
            referral_code=new_referral_code
        )
        db.session.add(user)
        db.session.commit()

        return render_template('signup_success.html', referral_code=new_referral_code)

    # Handle GET request for rendering the signup form
    referral_code = request.args.get('ref', None)  # Auto-fill referral code if provided in query string
    return render_template('signup.html', referral_code=referral_code)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get login credentials
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate credentials
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return render_template('login.html', error="Invalid email or password"), 401

        # Successful login
        return render_template('dashboard.html', user=user)

    # Render the login form for GET requests
    return render_template('login.html')
