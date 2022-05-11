import asyncio

from db.base import Base, engine
from models import models


async def init_models():  # Я бы, конечно, использовал alembic, но по ТЗ можно и так =)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_models())
