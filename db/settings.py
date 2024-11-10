class DatabaseSettings:
    pass


class PostgresSettings(DatabaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_PREFIX: str
    POSTGRES_ASYNC_PREFIX: str

    def __init__(
            self, 
            POSTGRES_USER: str = "postgres",
            POSTGRES_PASSWORD: str = "postgres",
            POSTGRES_SERVER: str = "localhost",
            POSTGRES_PORT: int = 5432,
            POSTGRES_DB: str = "postgres",
            POSTGRES_PREFIX: str = "postgresql://",
            POSTGRES_ASYNC_PREFIX: str = "postgresql+asyncpg://"
    ) -> None:
        super().__init__()
        self.POSTGRES_USER = POSTGRES_USER
        self.POSTGRES_PASSWORD = POSTGRES_PASSWORD
        self.POSTGRES_SERVER = POSTGRES_SERVER
        self.POSTGRES_PORT = POSTGRES_PORT
        self.POSTGRES_DB = POSTGRES_DB
        self.POSTGRES_PREFIX = POSTGRES_PREFIX
        self.POSTGRES_ASYNC_PREFIX = POSTGRES_ASYNC_PREFIX
    

    @property
    def POSTGRES_URI(self) -> str:
        return f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
