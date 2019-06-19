import os

import connexion
from flask_pymongo import PyMongo

from api_settings.mongo import mongo_uri


basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app.add_api("rest_api.yml")

flask_app = connex_app.app

flask_app.config["MONGO_URI"] = mongo_uri

mongo = PyMongo(flask_app)

