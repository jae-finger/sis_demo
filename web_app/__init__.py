# web_app/__init__.py

import os
from flask import Flask
from dotenv import load_dotenv

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.student_routes import student_routes

load_dotenv()
DATABASE_URI = os.getenv("DATABASE_URI")


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sis_vis_dev.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(student_routes)
    return app


if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
