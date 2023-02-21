from app import db

class Order_detail(db.Model):
    __tablename__ = 'order_detail'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)
