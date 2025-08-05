from src import db
from .base import BaseModel

class Order(BaseModel):
    """Order model for tracking purchases"""
    __tablename__ = 'orders'

    user_id = db.Column(db.Integer, db.ForignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)

    #relationships
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    items = db.relationship('OrderItem', backref='order', lazy=True)

    @property
    def calculate_total(self):
        """Calculate total amount of order"""
        return sum(item.subtotal for item in self.items)
    
class OrderItem(BaseModel):
    """OrderItem model for items in an order"""
    __tablename__ = 'order_items'

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    #relationships
    product = db.relationship('Product')

    @property
    def subtotal(self):
        """Calculate subtotal for item"""
        return self.quantity * self.price