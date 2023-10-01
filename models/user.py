from sqlalchemy import (
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .database import db


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32),
                                      unique=False,
                                      nullable=False)
    username: Mapped[str] = mapped_column(String(32),
                                          unique=False,
                                          nullable=False)
    email: Mapped[str] = mapped_column(String(120),
                                       nullable=False,
                                       unique=False)

    phone: Mapped[str] = mapped_column(String(32),
                                       nullable=True,
                                       unique=False)
    website: Mapped[str] = mapped_column(String(32),
                                         nullable=True,
                                         unique=False)


    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, username={self.username!r})"
