from typing import List
import asyncio
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from db.base import Base, engine, LocalAsyncSession
from models import models

# Всё это заменяется библиотекой Faker, но в рамках тест.задания я не стал добавлять ещё одну зависимость.
USER_INFO = {
    "first_name": "TestUserFM",
    "last_name": "TestUserLM",
    "email": "test@test.test"
}
SHOP_INFO = {
    "name": "TestShopName",
    "address": "TestShopAddress"
}
BOOK_INFO = {
    "name": "TestBook",
    "author": "TestAuthor",
    "release_date": datetime.now()
}
ORDER_INFO = {
    "reg_date": datetime.now()
}
ORDER_ITEM_INFO = {
    "quantity": 5
}


async def fill_db(session: AsyncSession) -> None:
    user = models.User(**USER_INFO)
    shop = models.Shop(**SHOP_INFO)
    book = models.Book(**BOOK_INFO)
    session.add_all([user, shop, book])
    await session.flush()

    order = models.Order(user_id=user.id, **ORDER_INFO)
    session.add(order)
    await session.flush()

    order_item = models.OrderItem(
        order_id=order.id,
        book_id=book.id,
        shop_id=shop.id,
        **ORDER_ITEM_INFO,
    )
    session.add_all([user, shop, book, order, order_item])
    return None


async def init_models():  # Я бы, конечно, использовал alembic, но по ТЗ можно и так =)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async with LocalAsyncSession() as session:
        await fill_db(session)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(init_models())
