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


class ShopScheme(BaseScheme):
    name: str
    address: str


class BookScheme(BaseScheme):
    name: str
    author: str
    release_date: date


class OrderItemScheme(BaseScheme):
    quantity: int
    book: BookScheme
    shop: ShopScheme
    pass


class OrderOutputScheme(BaseScheme):
    items: List[OrderItemScheme]
    reg_date: datetime
    user_id: int
