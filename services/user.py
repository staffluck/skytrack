from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import User


async def get_user_by_id(session: AsyncSession, id: int) -> User:
    q = select(User).where(User.id == id)
    result = await session.execute(q)
    return result.scalars().first()