from app import db

class Cart_item(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)
