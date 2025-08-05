from src import db
from .base import BaseModel

class Product(BaseModel):
    """Product model for inventory items"""
    __tablename__ = 'products'

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    sku = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(50))

    def update_quantity(self, amount):
        """update product quantity"""
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = new_quantity
        db.session.commit()

    @classmethod
    def search(cls, query):
        """Search products by name or description"""
        return cls.query.filter(
            db.or_(
                cls.name.ilike(f'%{query}%'),
                cls.description.ilike(f'%{query}%')
            )
        ).all()
    
    def __repr__(self):
        return f'<Product {self.name}>'
    