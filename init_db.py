import asyncio

from db.base import Base, engine
from models import base, user  # noqa Для подгрузки всех нужных моделей


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_models())
