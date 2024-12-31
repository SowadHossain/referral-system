---

# Referral System

A **Referral System** built using Flask and SQLite3, designed to allow users to:
- Sign up and generate unique referral codes.
- Use referral links to refer others.
- Track referral counts and view a leaderboard.
- Log in to access their personalized user dashboard.

This project is structured for scalability and modularity, making it easy to extend and maintain.

---

## **Features**

### **Core Features**
1. **User Registration**:
   - Users can sign up with their name, email, and password.
   - Each user is assigned a unique referral code.
   - Referral codes can be shared via personalized links to invite others.

2. **Referral System**:
   - Users can sign up using a referral code or link.
   - Referrers get credit for successful referrals.
   - Referral data is stored in the database for tracking.

3. **Leaderboard**:
   - Displays users ranked by their referral count.
   - Supports caching to reduce database queries and improve performance.

4. **User Login**:
   - Registered users can log in securely using their email and password.
   - Logged-in users can view their dashboard, which includes:
     - Their referral code.
     - Total referrals made.
     - A personalized referral link.

---

### **Advanced Features**
1. **Scalability**:
   - Modular codebase with Blueprints for different functionalities.
   - Supports pagination for the leaderboard to handle a large number of users.

2. **Caching**:
   - Leaderboard data is cached to improve performance and reduce server load.

3. **Security**:
   - Passwords are hashed using `werkzeug.security`.
   - Input validation to prevent invalid data submissions.

4. **Database Migrations**:
   - Uses Flask-Migrate for database versioning, allowing for seamless schema updates.

5. **Session Management** (Planned):
   - Persistent user sessions using Flask-Login.

6. **Responsive Design** (Planned):
   - Mobile-friendly UI for a better user experience.

---

## **Technologies Used**

| Technology        | Purpose                             |
|--------------------|-------------------------------------|
| **Flask**         | Web framework for backend logic.   |
| **SQLite3**       | Database for storing user and referral data. |
| **Flask-SQLAlchemy** | ORM for database operations.      |
| **Flask-Migrate** | Handles database migrations.       |
| **Flask-Caching** | Implements caching for better performance. |
| **Werkzeug**      | Password hashing and security.     |
| **Jinja2**        | Templating engine for HTML pages.  |

---

## **Project Structure**

```
referral-system/
├── app.py                # Main Flask application
├── extensions.py         # Flask extensions (SQLAlchemy, Cache, Migrate)
├── models.py             # Database models for User and Referral
├── auth/                 # Authentication module
│   ├── __init__.py       # Blueprint registration
│   ├── routes.py         # Routes for signup and login
├── referral/             # Referral module
│   ├── __init__.py       # Blueprint registration
│   ├── routes.py         # Referral processing and leaderboard
│   ├── utils.py          # Helper functions for referral logic
├── templates/            # HTML templates
│   ├── signup.html       # Signup form
│   ├── login.html        # Login form
│   ├── signup_success.html  # Signup success page
│   ├── leaderboard.html  # Leaderboard page
│   ├── dashboard.html    # User dashboard
├── static/               # Static files (CSS, JS, Images)
├── migrations/           # Database migration files
├── database.db           # SQLite3 database
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.7 or higher
- pip (Python package manager)

### **Steps to Run Locally**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/referral-system.git
   cd referral-system
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your browser and navigate to:
   - `http://127.0.0.1:5000/auth/signup`: Signup page.
   - `http://127.0.0.1:5000/auth/login`: Login page.
   - `http://127.0.0.1:5000/referral/leaderboard`: Leaderboard.

---

## **Database Schema**

### **User Table**
| Column           | Type        | Description                       |
|------------------|-------------|-----------------------------------|
| id               | Integer     | Primary key                      |
| name             | String      | User’s name                      |
| email            | String      | Unique email address             |
| password         | String      | Hashed password                  |
| referral_code    | String      | Unique referral code             |
| referrals_count  | Integer     | Total referrals made by the user |
| created_at       | DateTime    | Timestamp of user creation       |

### **Referral Table**
| Column         | Type        | Description                      |
|----------------|-------------|----------------------------------|
| id             | Integer     | Primary key                     |
| referrer_id    | Integer     | Foreign key linking to `User.id`|
| referred_email | String      | Email of the referred user      |
| created_at     | DateTime    | Timestamp of referral creation  |

---

## **API Endpoints**

### **1. Signup**
- **URL**: `/auth/signup`
- **Method**: `GET` / `POST`
- **Description**:
  - Displays the signup form (GET).
  - Registers a new user and generates a referral code (POST).

### **2. Login**
- **URL**: `/auth/login`
- **Method**: `GET` / `POST`
- **Description**:
  - Displays the login form (GET).
  - Authenticates users (POST).

### **3. Process Referral**
- **URL**: `/referral/process_referral`
- **Method**: `POST`
- **Description**:
  - Updates the referral table and the referrer’s referral count when a new user signs up using a referral code.

### **4. Leaderboard**
- **URL**: `/referral/leaderboard`
- **Method**: `GET`
- **Description**:
  - Displays a leaderboard of users ranked by referral counts.

---

## **Future Enhancements**

1. **Session Management**:
   - Use Flask-Login for persistent user sessions.

2. **Password Reset**:
   - Add a "Forgot Password" feature for users.

3. **Admin Dashboard**:
   - Enable admin access to manage users and view analytics.

4. **Email Notifications**:
   - Notify users when they successfully refer someone.

5. **Rewards System**:
   - Offer rewards based on referral counts.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## **License**
This project is licensed under the MIT License.

---

