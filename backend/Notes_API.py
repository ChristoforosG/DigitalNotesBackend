import re
from unittest import result
from flask import jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    JWTManager
)
import uuid
from datetime import datetime
import User

def notes_show():
    user = get_jwt_identity()
    collection = User.access_db()["Note"]
    list_of_notes = list(collection.find({"user": user}))
    return jsonify(sorted(list_of_notes, key=lambda x: x["date"], reverse=True))

def note_insert(data):
    user = get_jwt_identity()
    collection = User.access_db()["Note"]
    try:
        data["title"] = data["title"]
        data["text"] = data["text"]
        data["keywords"] = data["keywords"]
        data["user"] = user
        data["date"] = datetime.now().strftime("%d/%m/%Y")
        data["_id"] = uuid.uuid4().hex
        collection.insert_one(data)
        return jsonify({"response": "Note inserted successfully"})
    except Exception as e:
        return jsonify({"response": "Wrong note info"}), 400


def note_delete(title):
    user = get_jwt_identity()
    collection = User.access_db()["Note"]
    results = list(collection.find({"user": user,"title": title}))
    if results == []:
        return jsonify({"response": "No note found to be deleted"})
    collection.delete_many({"user": user,"title": title})
    return jsonify({"response": "Deleted {} notes".format(len(results))})

def note_search(key, value):
    user = get_jwt_identity()
    collection = User.access_db()["Note"]
    if key == "title":
        results = list(collection.find({"user": user,key: value}))
        return jsonify(results)
    results = list(collection.find({"user": user}))
    response = []
    for result in results:
        if value in result[key].replace(" ","").split(","):
            response.append(result)
    return jsonify(response)

def note_change(title, data):
    for key in data.keys():
            if key not in ("title", "text", "keywords"):
                return jsonify({"response": "Wrong note info"}), 400
    user = get_jwt_identity()
    collection = User.access_db()["Note"]
    results = list(collection.find({"user": user,"title": title}))
    if results == []:
        return jsonify({"response": "No note found to be modified"})
    try:
        collection.update_many({"user": user,"title": title}, {"$set": data})
        return jsonify({"response": "Modified {} notes".format(len(results))})
    except Exception as e:
        return jsonify({"response": "Wrong update info"}), 400
        