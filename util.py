from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

import jsonplaceholder_requests
from models import User  # , Post


async def get_users():

    return await jsonplaceholder_requests.fetch_api(jsonplaceholder_requests.USERS_DATA_URL)


async def get_posts():
    return await jsonplaceholder_requests.fetch_api(jsonplaceholder_requests.POSTS_DATA_URL)


def populate_users(database: SQLAlchemy, users_list: list[User]) -> list:
    stmt = select(User).order_by(User.id)
    users_from_db_list: List[User] = database.session.scalars(statement=stmt)
    users_from_db_list = list(users_from_db_list)
    if len(users_from_db_list) == 0:
        database.session.add_all(users_list)
        database.session.commit()
    return users_list
