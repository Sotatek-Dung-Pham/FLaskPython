from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=True)
    images = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=True)
    discount = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)
