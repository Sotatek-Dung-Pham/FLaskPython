from app import db
from models.user import User
from models.blacklist_token import BlacklistToken

def get_user_by_email(email):
    user = User.query\
        .filter_by(email = email)\
        .first()

    return user

def get_user_by_public_id(public_id):
    user = User.query\
        .filter_by(public_id = public_id)\
        .first()

    return user

def create_user_by_email_and_password(email, password):
    user = User(
        email = email,
        password = password
    )

    # insert user
    db.session.add(user)
    db.session.commit()

    return user

def get_all_user():
    return User.query.all()

def create_blacklist_token_by_token(token):
    if (BlacklistToken.check_blacklist(token)):
        return False

    black_list_token = BlacklistToken(
        token = str(token)
    )

    db.session.add(black_list_token)
    db.session.commit()

    return black_list_token
