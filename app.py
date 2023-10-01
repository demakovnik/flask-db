from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from models import db
from views.users import users


def create_app():
    application = Flask(__name__)
    config_name = getenv("CONFIG_NAME", "Config")
    application.config.from_object(f"config.{config_name}")
    db.init_app(app=application)
    application.register_blueprint(users)
    return application


app = create_app()

migrate = Migrate(app=app, db=db)




@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")
