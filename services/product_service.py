from app import db
from models.product import Product
from sqlalchemy import text

def get_all_product():
    return Product.query.order_by(text('id asc'))

def get_product_by_id(id):
    product = Product.query\
        .filter_by(id = id)\
        .first()

    return product
