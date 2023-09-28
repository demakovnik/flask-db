"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from asyncio import run, gather

import jsonplaceholder_requests
from models import init_models, User, Post, Session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_users():
    return await jsonplaceholder_requests.fetch_api(jsonplaceholder_requests.USERS_DATA_URL)


async def get_posts():
    return await jsonplaceholder_requests.fetch_api(jsonplaceholder_requests.POSTS_DATA_URL)


async def create_users(
        session: AsyncSession,
        users: list[dict],
) -> list[User]:
    result: list[User] = []
    for user in users:
        created_user = User(id=user['id'],
                            name=user['name'],
                            username=user['username'],
                            email=user['email'],
                            address=user['address'],
                            phone=user['phone'],
                            website=user['website'],
                            company=user['company'])
        result.append(created_user)
        session.add(created_user)
    await session.commit()
    return result


async def create_posts(
        session: AsyncSession,
        posts: list[dict],
) -> list[Post]:
    result: list[Post] = []
    for post in posts:
        created_post = Post(id=post['id'],
                            title=post['title'],
                            body=post['body'],
                            user_id=post['userId'], )
        result.append(created_post)
        session.add(created_post)
    await session.commit()
    return result


async def async_main():
    await init_models()
    users = await get_users()
    posts = await get_posts()
    tasks = [create_users(session=Session(), users=users), create_posts(session=Session(), posts=posts)]
    return await gather(*tasks)


def main():
    users_data, posts_data = run(async_main())

if __name__ == "__main__":
    main()
