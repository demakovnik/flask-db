__all__ = ("app",)

from asyncio import run

from app import app
from models import User, db
from util import get_users, populate_users

if __name__ == "__main__":
    with app.app_context():
        usrs = run(main=get_users())
        usrs = list(map(lambda item: User(
            name=item['name'],
            username=item['username'],
            email=item['email'],
            phone=item['phone'],
            website=item['website']), usrs))
        populate_users(database=db, users_list=usrs)

    app.run(
        host="0.0.0.0",
        port=80,
        debug=False,
    )
