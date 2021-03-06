# web_app/__init__.py

import os
from flask import Flask
from dotenv import load_dotenv

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.school_routes import school_routes
from web_app.routes.vis_routes import vis_routes

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")

def create_app(): # Working base create app
    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(school_routes)
    app.register_blueprint(vis_routes)
    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
