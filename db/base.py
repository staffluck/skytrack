from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./project_db.db"

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
AsyncLocalSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()