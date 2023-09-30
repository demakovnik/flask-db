__all__ = ("app",)

from asyncio import run

from app import app
from models import User #, Post
from util import get_posts, get_users, populate_users #, populate_posts

if __name__ == "__main__":

    # users = run(main=get_users())
    # users = list(map(lambda item: User(
    #     id=item['id'],
    #     name=item['name'],
    #     username=item['username'],
    #     email=item['email'],
    #     #address=item['address'],
    #     phone=item['phone'],
    #     website=item['website']), users))
    #     #company=item['company']), users))
    #
    # populate_users(users_list=users)
    # posts = run(main=get_posts())
    # posts = list(map(lambda item: Post(
    #     id=item['id'],
    #     title=item['title'],
    #     body=item['body'],
    #     user_id=int(item['userId'])
    # ), posts))
    #
    # populate_posts(posts_list=posts)
    app.run(
        # host="localhost",
        # port=5000,
        debug=True,
    )

