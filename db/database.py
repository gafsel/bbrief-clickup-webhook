from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from db.settings import DatabaseSettings, PostgresSettings

import os


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self, settings: DatabaseSettings, run_async: bool = False) -> None:
        self.settings = settings
        self.run_async = run_async
        self.Base = Base

        if isinstance(settings, PostgresSettings):
            if self.run_async:
                self.db_uri = (
                    f"{self.settings.POSTGRES_ASYNC_PREFIX}{self.settings.POSTGRES_URI}"
                )
                self.engine = create_async_engine(self.db_uri)
                self.session = sessionmaker(
                    bind=self.engine,
                    class_=AsyncSession,
                    autocommit=False,
                    autoflush=False,
                    expire_on_commit=False,
                )
            else:
                self.db_uri = (
                    f"{self.settings.POSTGRES_PREFIX}{self.settings.POSTGRES_URI}"
                )
                self.engine = create_engine(self.db_uri)
                self.session = sessionmaker(
                    bind=self.engine, autocommit=False, autoflush=False
                )
        else:
            raise NotImplementedError("Only PostgresSettings are currently supported.")

    def get_session(self):
        return self.session()

    async def async_get_session(self):
        if not self.run_async:
            raise RuntimeError("The database is configured for synchronous operation.")
        async with self.session() as session:
            yield session


def new() -> Database:
    return Database(
        settings=PostgresSettings(
            POSTGRES_USER=os.getenv("POSTGRES_USER"),
            POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD"),
            POSTGRES_SERVER=os.getenv("POSTGRES_SERVER"),
            POSTGRES_PORT=int(os.getenv("POSTGRES_PORT")),
            POSTGRES_DB=os.getenv("POSTGRES_DB"),
            POSTGRES_PREFIX="postgresql://",
            POSTGRES_ASYNC_PREFIX="postgresql+asyncpg://",
        )
    )