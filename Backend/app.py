import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from extensions import db, migrate, cache
from auth.routes import auth_bp
from referral.routes import referral_bp
# from base.routes import base_bp  # If you're still using base_bp for something else

def create_app():
    # We tell Flask that our static files (including index.html) are in 'static/'
    # static_url_path='' means they are served at the root (e.g., '/index.html').
    app = Flask(__name__, static_folder='static', static_url_path='')
    CORS(app)

    # -------------------------------------------------------------------------
    # 1. Configuration
    # -------------------------------------------------------------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CACHE_TYPE'] = 'SimpleCache'

    # -------------------------------------------------------------------------
    # 2. Initialize Extensions
    # -------------------------------------------------------------------------
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    # -------------------------------------------------------------------------
    # 3. Register Blueprints (Backend Routes)
    # -------------------------------------------------------------------------
    # If you want these routes under '/auth' and '/referral' respectively:
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(referral_bp, url_prefix='/referral')
    # If you have a base_bp, only use it if it's NOT calling render_template('base.html')
    # app.register_blueprint(base_bp)

    # Create all database tables if they don't exist
    with app.app_context():
        db.create_all()

    # -------------------------------------------------------------------------
    # 4. Serve React's index.html and Handle Client-Side Routing
    # -------------------------------------------------------------------------
    @app.route('/')
    def index():
        """
        Serve the main index.html for the React app.
        """
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/<path:path>')
    def catch_all(path):
        """
        1) If the requested file exists in /static, serve it (images, CSS, JS, etc.).
        2) Otherwise, serve index.html so the React router can handle the route.
        """
        file_path = os.path.join(app.static_folder, path)
        if os.path.exists(file_path):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, 'index.html')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
