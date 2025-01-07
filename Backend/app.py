from flask import Flask
from extensions import db, migrate, cache
from auth.routes import auth_bp
from referral.routes import referral_bp
from base.routes import base_bp  # Import base routes
from flask_cors import CORS

app = Flask(__name__)
application = app
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

# **Add a simple '/' route for debugging**
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask Backend Home</title>
    </head>
    <body>
        <h1>Welcome to the Flask Backend!</h1>
        <p>This is a simple HTML page for debugging purposes.</p>
    </body>
    </html>
    """
    return html_content

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run()