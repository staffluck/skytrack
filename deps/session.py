from sqlalchemy.ext.asyncio import AsyncSession
from db.base import LocalAsyncSession


async def get_session() -> AsyncSession:
    async with LocalAsyncSession() as session:
        yield session
