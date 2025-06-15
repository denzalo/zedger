# init_db.py – one-time database bootstrap
from app import db, app

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created.")
