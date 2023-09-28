from typing import List

from sqlalchemy import (
    JSON,
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from .database import db


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32),
                                      unique=True,
                                      nullable=False)
    username: Mapped[str] = mapped_column(String(32),
                                          unique=True,
                                          nullable=False)
    email: Mapped[str] = mapped_column(String(120),
                                       nullable=False,
                                       unique=True)
    address: Mapped[dict] = mapped_column(JSON(),
                                          nullable=True,
                                          unique=False)
    phone: Mapped[str] = mapped_column(String(32),
                                       nullable=True,
                                       unique=False)
    website: Mapped[str] = mapped_column(String(32),
                                         nullable=True,
                                         unique=False)
    company: Mapped[dict] = mapped_column(JSON(),
                                          nullable=True,
                                          unique=False)
    posts: Mapped[List["Post"]] = relationship(back_populates="users",
                                               uselist=True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, username={self.username!r})"
