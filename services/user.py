from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import User


async def get_user_by_id(session: AsyncSession, id: int) -> User:
    result = await session.execute(select(User).where(User.id == id))
    return result.scalars().first()
