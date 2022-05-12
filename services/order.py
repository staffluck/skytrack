from datetime import datetime
from typing import List, Union

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import Order, OrderItem


async def get_user_orders(session: AsyncSession, user_id: int) -> List[Order]:
    q = select(Order).options(joinedload(Order.items).joinedload(OrderItem.shop)).options(joinedload(Order.items).joinedload(OrderItem.book)).where(Order.user_id == user_id)
    result = await session.execute(q)
    result.unique()

    return result.scalars().all()


async def get_order_by_id(session: AsyncSession, order_id: int) -> Union[Order, None]:
    q = select(Order).options(joinedload(Order.items).joinedload(OrderItem.shop)).options(joinedload(Order.items).joinedload(OrderItem.book)).where(Order.id == order_id)
    result = await session.execute(q)

    return result.scalars().first()


async def add_order(session: AsyncSession, user_id: int, items: List[dict]) -> Order:
    order = Order(reg_date=datetime.now(), user_id=user_id)
    session.add(order)
    await session.flush()

    for item in items:
        order_item = OrderItem(**item, order_id=order.id)
        session.add(order_item)

    return order
