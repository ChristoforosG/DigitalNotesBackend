import collections
from gc import collect
from pydoc import doc
import re
from bson import ObjectId
from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient
from datetime import datetime
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager
)
import User
import Notes_API

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "dddfsdfweffweffghrthrt"  
jwt = JWTManager(app)

@app.route('/')
def home():
    return "Digital Notes"

@app.route('/sign-up', methods=['POST'])
def sign_up():
    return User.sign_up(request.get_json())

@app.route('/sign-in', methods=['POST'])
def sign_in():
    return User.sign_in(request.get_json())

@app.route('/notes-show', methods=["GET"])
@jwt_required(fresh=True)
def notes_show():
    return Notes_API.notes_show()

@app.route("/note-insert", methods=["POST"])
@jwt_required(fresh=True)
def note_insert():
    return Notes_API.note_insert(request.get_json())

@app.route("/note-search-title", methods=["GET"])
@jwt_required(fresh=True)
def note_search_title():
    try:
        title = request.args.get("title")
        return Notes_API.note_search("title", title)
    except Exception as e:
        return jsonify({"Response": "Bad Request"}), 400

@app.route("/note-search-keyword", methods=["GET"])
@jwt_required(fresh=True)
def note_search_keyword():
    try:
        keyword = request.args.get("keyword")
        return Notes_API.note_search("keywords", keyword)
    except Exception as e:
        return jsonify({"Response": "Bad Request"}), 400

@app.route("/note-change/<string:title>", methods=["PUT"])
@jwt_required(fresh=True)
def note_change(title):
    return Notes_API.note_change(title, request.get_json())

@app.route("/note-delete", methods=["DELETE"])
@jwt_required(fresh=True)
def note_delete():
    try:
        title = request.args.get("title")
        return Notes_API.note_delete(title)
    except Exception as e:
        return jsonify({"Response": "Bad Request"}), 400
    
@app.route("/user-delete", methods=["DELETE"])
@jwt_required(fresh=True)
def user_delete():
    return User.user_delete()

@app.route("/admin-delete/<user_name>", methods=["DELETE"])
@jwt_required(fresh=True)
def admin_delete(user_name):
    return User.admin_delete(user_name)

@app.route("/admin-add/", methods=["POST"])
@jwt_required(fresh=True)
def admin_add():
    return User.admin_add(request.get_json())

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)