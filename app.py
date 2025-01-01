from flask import Flask
from extensions import db, migrate, cache
from auth.routes import auth_bp
from referral.routes import referral_bp

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CACHE_TYPE'] = 'SimpleCache'

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(referral_bp, url_prefix='/referral')

    with app.app_context():
        db.create_all()

    return app
    

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


