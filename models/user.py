from app import db, login_manager, bcrypt
from flask_login import UserMixin
import datetime
import uuid

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, password):
        self.public_id = str(uuid.uuid4())
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode()
        self.registered_on = datetime.datetime.now()

    def __repr__(self):
        return '<id {}>'.format(self.id)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
