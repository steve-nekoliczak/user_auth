from json import loads

from bson.json_util import dumps, RELAXED_JSON_OPTIONS

from models import User


def register(username, password, email):
    from config import mongo
    result = mongo.db.user.find_one({'username': username})
    if result is not None:
        return "Username already exists.", 400
    result = mongo.db.user.find_one({'email': email})
    if result is not None:
        return "Email already registered.", 400

    user = User(username, password, email)
    user_dict = user.to_dict()

    mongo.db.user.insert(user_dict)

    return "Successfully registered " + username, 200


def get_info(username):
    from config import mongo
    result = mongo.db.user.find_one({'username': username})
    if result is None:
        return "Username not found.", 400

    json_result = loads(dumps(result, json_options=RELAXED_JSON_OPTIONS))
    return json_result, 200

