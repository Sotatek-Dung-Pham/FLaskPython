from app import db
from sqlalchemy import text
from models.user import User
from models.blacklist_token import BlacklistToken
from models.product import Product
from models.cart import Cart
from models.cart_item import Cart_item

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

def get_all_product():
    return Product.query.order_by(text('id asc'))

def get_product_by_id(id):
    product = Product.query\
        .filter_by(id = id)\
        .first()

    return product

def add_cart_by_product_id_and_quantity(product_id, quantity, user_id):
    cart = get_cart_by_user_id(user_id)
    if not cart:
        cart = Cart(
            user_id = user_id
        )
        add_cart(cart)

    cart_item = get_cart_item_isfalse_status(cart.id, product_id)
    if not cart_item:
        cart_item = Cart_item(
            cart_id = cart.id,
            product_id = product_id,
            quantity = quantity,
            status = False
        )
        add_cart_item(cart_item)
    else:
        args = {
            'quantity': 1
        }
        update_cart_item(cart_item, args)

    return cart_item

def get_cart_by_user_id(user_id):
    cart = Cart.query\
        .filter_by(user_id = user_id)\
        .first()

    return cart

def get_cart_item_isfalse_status(cart_id, product_id):
    cart_item = Cart_item.query\
        .filter_by(cart_id = cart_id, product_id = product_id, status = False)\
        .first()

    return cart_item

def add_cart(cart):
    db.session.add(cart)
    db.session.commit()

    return cart

def add_cart_item(cart_item):
    db.session.add(cart_item)
    db.session.commit()

    return cart_item

def update_cart_item(cart_item, datas):
    cart_item.quantity = datas['quantity']
    db.session.commit()

    return cart_item

def count_item_cart(user_id):
    cart_item = Cart_item.query\
        .join(Cart)\
        .filter_by(user_id = user_id)\
        .count()

    return cart_item
