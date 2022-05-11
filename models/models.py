from sqlalchemy import Column, String, Date, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    orders = relationship("Order", backref="user")


class Book(BaseModel):
    __tablename__ = "books"

    name = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    author = Column(String, nullable=False)


class Shop(BaseModel):
    __tablename__ = "shops"

    name = Column(String, nullable=False)
    address = Column(String, nullable=False)


class Order(BaseModel):
    __tablename__ = "orders"

    reg_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    items = relationship("OrderItem", back_populates="order")


class OrderItem(BaseModel):
    __tablename__ = "order_items"

    quantity = Column(Integer, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    shop_id = Column(Integer, ForeignKey("shops.id"), nullable=False)

    order = relationship("Order", back_populates="items")
    book = relationship("Book")
    shop = relationship("Shop")
