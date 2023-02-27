from app import db

class Cart_item(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Boolean, nullable=True)

    def __init__(self, cart_id, product_id, quantity, status):
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)
