"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    JSON,
)

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    relationship,
    sessionmaker
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(
    url=PG_CONN_URI,
    echo=False,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        # prefix = config.TABLES_PREFIX
        # return f"{prefix}{cls.__name__.lower()}s"
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)

Session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class User(Base):
    name = Column(
        String(32),
        nullable=False,
        unique=True
    )
    username = Column(
        String(32),
        nullable=False,
        unique=True
    )
    email = Column(
        String(120),
        nullable=False,
        unique=True
    )
    address = Column(
        JSON,
        nullable=True,
        unique=False
    )
    phone = Column(
        String(32),
        nullable=True,
        unique=False
    )
    website = Column(
        String(32),
        nullable=True,
        unique=False
    )
    company = Column(
        JSON,
        nullable=True,
        unique=False
    )
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, email={self.email!r}, address={self.address!r})"

    def __repr__(self):
        return str(self)


class Post(Base):
    title = Column(
        String(120),
        nullable=False,
        unique=False,
        # index=True,
    )
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    @property
    def body_len(self):
        return len(self.body)

    def __str__(self):
        return f"Post(id={self.id}, title={self.title!r})"

    def __repr__(self):
        """
        :return:
        """
        return str(self)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


