from sqlalchemy import (
    ForeignKey,
    String,
Text
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from .database import db


class Post(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120),
                                       nullable=False,
                                       unique=False, )
    body: Mapped[str] = mapped_column(Text,
                                      nullable=False,
                                      unique=False,
                                      default="",
                                      server_default="")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),
                                         unique=False,
                                         nullable=False)
    user: Mapped["User"] = relationship(back_populates="posts",
                                        cascade=True,
                                        uselist=False)

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
