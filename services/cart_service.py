from app import db
from models.cart import Cart
from models.cart_item import Cart_item
from models.product import Product

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

def get_all_cart_item_isfalse_by_user_id(user_id):
    cart_item = db.session.query(Cart_item, Cart, Product)\
        .join(Cart)\
        .join(Product)\
        .filter(Cart.user_id == user_id, Cart_item.status == False)\
        .all()

    return cart_item

def count_cart_item(user_id):
    cart_item = Cart_item.query\
        .join(Cart)\
        .filter_by(user_id = user_id)\
        .count()

    return cart_item

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
