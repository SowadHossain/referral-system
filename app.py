from flask import Flask, request, jsonify, render_template, redirect
from models import db, User, Referral, init_app
from referral import generate_referral_code, increment_referrals_count

app = Flask(__name__)
init_app(app)

with app.app_context():
    db.create_all()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        referral_code = request.form.get('referral_code', None)  # Get referral code from form

        # Check if the user already exists
        if User.query.filter_by(email=email).first():
            return "Email already registered", 400

        # Generate a unique referral code for the new user
        new_referral_code = generate_referral_code()

        # Handle referral logic
        if referral_code:
            referrer = User.query.filter_by(referral_code=referral_code).first()
            if referrer:
                # Increment referrer's referral count
                increment_referrals_count(referrer.id)

                # Add a record to the Referral table
                referral = Referral(referrer_id=referrer.id, referred_email=email)
                db.session.add(referral)

        # Save the new user
        user = User(name=name, email=email, password=password, referral_code=new_referral_code)
        db.session.add(user)
        db.session.commit()

        return render_template('success.html', referral_code=new_referral_code)

    # Auto-fill referral code if provided in query parameters
    referral_code = request.args.get('ref', None)
    return render_template('signup.html', referral_code=referral_code)


@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    users = User.query.order_by(User.referrals_count.desc()).all()
    leaderboard_data = [{'name': user.name, 'referrals_count': user.referrals_count} for user in users]
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

if __name__ == "__main__":
    app.run(debug=True)