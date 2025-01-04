from flask import Flask
from extensions import db, migrate, cache
from auth.routes import auth_bp
from referral.routes import referral_bp
from base.routes import base_bp  # Import base routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)
    
    # Load configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CACHE_TYPE'] = 'SimpleCache'

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    # Register blueprints
    app.register_blueprint(base_bp)  # Base routes
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Auth routes
    app.register_blueprint(referral_bp, url_prefix='/referral')  # Referral routes

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
