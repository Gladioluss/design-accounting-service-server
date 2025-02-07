from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlmodel.ext.asyncio.session import AsyncSession

from app.configs.settings.settings import settings


engine = create_async_engine(
    url=str(settings.ASYNC_DATABASE_URI),
    echo=False,
    future=True,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=64,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
