from typing import List

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

import jsonplaceholder_requests
from config import Config
from models import User #, Post


async def get_users():
    return await jsonplaceholder_requests.fetch_api(jsonplaceholder_requests.USERS_DATA_URL)


async def get_posts():
    return await jsonplaceholder_requests.fetch_api(jsonplaceholder_requests.POSTS_DATA_URL)


def populate_users(users_list: list[User]) -> list:
    engine = create_engine(
        url=Config().SQLALCHEMY_DATABASE_URI,
        echo=False,
    )

    sess = sessionmaker(bind=engine,
                        expire_on_commit=False,
                        class_=Session)

    with sess() as session:
        stmt = select(User).order_by(User.id)
        users_from_db_list: List[User] = session.scalars(statement=stmt)
        users_from_db_list = list(users_from_db_list)

    if len(users_from_db_list) == 0:
        with sess() as session:
            session.add_all(users_list)
            session.commit()
    return users_list

# def populate_posts(posts_list: list[Post]) -> list:
#     engine = create_engine(
#         url=Config().SQLALCHEMY_DATABASE_URI,
#         echo=False,
#     )
#
#     sess = sessionmaker(bind=engine,
#                         expire_on_commit=False,
#                         class_=Session)
#
#     with sess() as session:
#         stmt = select(Post).order_by(Post.id)
#         posts_from_db_list: List[Post] = session.scalars(statement=stmt)
#         posts_from_db_list = list(posts_from_db_list)
#
#     if len(posts_from_db_list) == 0:
#         with sess() as session:
#             session.add_all(posts_list)
#             session.commit()
#     return posts_list