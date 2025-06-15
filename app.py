from pathlib import Path
import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    render_template_string,
    redirect,
    request,
    url_for,
    flash,
)
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from models import db, User

# Load secrets
secret_path = Path("/etc/secrets/.env")
if secret_path.exists():        # Render
    load_dotenv(dotenv_path=secret_path)
else:                            # Local dev falls back to .env in repo root
    load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "dev-secret")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///zedger.db")

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Forward the .com domain to the .app domain
@app.before_request
def enforce_primary_domain():
    if request.host and request.host.endswith("zedgerapp.com"):
        url = request.url.replace("zedgerapp.com", "zedger.app")
        return redirect(url, code=301)

# Serve the index page
@app.route("/")
def index():
    return render_template("index.html")

# --- signup -------------------------------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"].lower()
        pwd = request.form["password"]
        if User.query.filter_by(email=email).first():
            flash("Email already registered", "error")
        else:
            user = User(email=email)
            user.set_password(pwd)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("dashboard"))
    return render_template_string(
        """
        <h2>Sign Up</h2>
        <form method="post">
          <input name=email type=email placeholder="Email" required><br>
          <input name=password type=password placeholder="Password" required><br>
          <button type=submit>Sign Up</button>
        </form>
        <a href="{{ url_for('login') }}">Have an account? Log in</a>
    """
    )

# --- login --------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].lower()
        pwd = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(pwd):
            login_user(user)
            return redirect(url_for("dashboard"))
        flash("Invalid credentials", "error")
    return render_template_string(
        """
        <h2>Log In</h2>
        <form method="post">
          <input name=email type=email placeholder="Email" required><br>
          <input name=password type=password placeholder="Password" required><br>
          <button type=submit>Log In</button>
        </form>
        <a href="{{ url_for('signup') }}">Need an account? Sign up</a>
    """
    )

# --- logout -------------------------------------------------
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# --- protected area -----------------------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    return f"Hello, {current_user.email}!  <a href='/logout'>Log out</a>"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT
    app.run(host="0.0.0.0", port=port)
