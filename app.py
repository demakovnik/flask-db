from os import getenv

from flask import Flask, request, render_template
from flask_migrate import Migrate

from models import db
from views.users import users

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
#config_name = getenv("CONFIG_NAME", "DevelopmentConfig")
config_name = getenv("CONFIG_NAME", "Config")
app.config.from_object(f"config.{config_name}")

db.init_app(app=app)
migrate = Migrate(app=app, db=db)

app.register_blueprint(users)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")
