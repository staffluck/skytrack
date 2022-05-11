from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import Order, OrderItem, User


async def get_user_orders(session: AsyncSession, user_id: int):
    q = select(Order).options(joinedload(Order.items).joinedload(OrderItem.shop)).options(joinedload(Order.items).joinedload(OrderItem.book)).where(User.id == user_id)
    result = await session.execute(q)
    result.unique()
    return result.scalars().all()
