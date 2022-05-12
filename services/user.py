from typing import Union

from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import User


async def get_user_by_id(session: AsyncSession, id: int) -> Union[User, None]:
    q = select(User).where(User.id == id)
    result = await session.execute(q)
    return result.scalars().first()


async def user_is_exists(session: AsyncSession, id: int) -> bool:
    q = select(exists(User)).where(User.id == id)
    result = await session.execute(q)
    return result.scalars()
