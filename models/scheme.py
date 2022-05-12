from datetime import datetime, date
from typing import List
from pydantic import BaseModel


class BaseScheme(BaseModel):

    class Config:
        orm_mode = True


class UserOutputScheme(BaseScheme):
    id: int
    first_name: str
    last_name: str
    email: str


class ShopOutputScheme(BaseScheme):
    name: str
    address: str


class BookOutputScheme(BaseScheme):
    name: str
    author: str
    release_date: date


class OrderItemOutputScheme(BaseScheme):
    quantity: int
    book: BookOutputScheme
    shop: ShopOutputScheme


class OrderOutputScheme(BaseScheme):
    items: List[OrderItemOutputScheme]
    reg_date: datetime
    user_id: int


class OrderItemInputScheme(BaseModel):
    quantity: int
    book_id: int
    shop_id: int


class OrderInputScheme(BaseModel):
    user_id: int
    items: List[OrderItemInputScheme]
