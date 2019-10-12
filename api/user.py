from json import loads

from bson.json_util import dumps, RELAXED_JSON_OPTIONS

from models.user import User


def register(email, password):
    from config import mongo
    result = mongo.db.user.find_one({'email': email})
    if result is not None:
        return "Email already registered.", 400

    user = User(email, password)
    user_dict = user.to_dict()

    mongo.db.user.insert(user_dict)

    return "Successfully registered " + email, 200


def get_info(email):
    from config import mongo
    result = mongo.db.user.find_one({'email': email})
    if result is None:
        return "Email not found.", 400

    json_result = loads(dumps(result, json_options=RELAXED_JSON_OPTIONS))
    return json_result, 200

