from typing import Sequence

from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest, NotFound

from models import db, User

users = Blueprint(
    "users",
    __name__,
    url_prefix="/users",
)

@users.get("/", endpoint="list")
def get_users_list():
    stmt = select(User).order_by(User.id)
    #users = db.session.execute(statement=stmt).scalars()
    users: Sequence[User] = db.session.scalars(statement=stmt)
    return render_template(
        "users/index.html",
        users=users,
    )


@users.route("/add/", methods={"GET", "POST"}, endpoint="add")
def create_user():
    if request.method == "GET":
        return render_template("users/add.html")

    name = request.form.get("user-name")
    username = request.form.get("user-username")
    email = request.form.get("user-email")
    phone = request.form.get("user-phone")
    website = request.form.get("user-website")
    if not name:
        raise BadRequest("field `user-name` required")
    user = User(name=name, username=username, email=email, phone=phone, website=website)
    print(user)
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        # BadRequest("Such product already exists!")
        flash(f"User {user.name!r} already exists!", category="warning")
        return redirect(request.path)

    flash(f"User {user.name!r} created")
    # return redirect("/users/")
    # url = url_for("products_app.list")
    url = url_for("users.detail", user_id=user.id)
    return redirect(url)

def get_userby_id(user_id: int) -> User:
    user: User = db.get_or_404(
        User,
        user_id,
        description=f"User #{user_id} not found!"
        )
    return user



@users.get("/<int:user_id>/", endpoint="detail")
def get_user_by_id(user_id: int):

    return render_template(
        "users/detail.html",
        user=get_userby_id(user_id=user_id),
    )

@users.route("<int:user_id>/confirm_delete/",
                    methods=["GET", "POST"],
                    endpoint="confirm_delete")
def confirm_delete_product(user_id: int):
    user = get_userby_id(user_id=user_id)
    if request.method == "GET":
        return render_template("users/confirm-delete.html",
                               user=user)
    name = user.name
    db.session.delete(user)
    db.session.commit()
    flash(f"User {name!r} deleted", category="danger")
    return redirect(url_for("users.list"))


