from flask import Blueprint, render_template

# Create a Blueprint for base routes
base_bp = Blueprint('base', __name__)

@base_bp.route('/')
def home():
    return render_template('base.html')  # Render the base template for the home page
