from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import event


DATABASE_URL = "sqlite+aiosqlite:///./project_db.db"

engine = create_async_engine(DATABASE_URL, echo=True)
LocalAsyncSession = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()


#  В sqlite3 по дефолту не работает ForeignKeyConstaint, нужно отдельно включать
def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')


# asyncengine пока что не поддерживает event
event.listen(engine.sync_engine, 'connect', _fk_pragma_on_connect)
