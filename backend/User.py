from flask import jsonify
import pymongo
from flask_jwt_extended import create_access_token,get_jwt_identity
import uuid
import hashlib

def access_db():
    client = pymongo.MongoClient(host='mongodb',
                        port=27017, 
                        username='root', 
                        password='pass',
                        authSource="admin")
    return client["DigitalNotes"]

def get_hash_value(value):
    m = hashlib.sha256()
    m.update(str.encode(value))
    return m.digest()

def sign_up(data):
    try:
        db = access_db()
        collection = db["User"]
        if collection.find_one({"user_name": data["user_name"]}):
             return jsonify({"response": "user name already exists"}), 409
        if collection.find_one({"e_mail": data["e_mail"]}):
             return jsonify({"response": "email already exists"}), 409
        data["is_admin"] = False
        data["password"] = get_hash_value(data["password"])
        data["_id"] = uuid.uuid4().hex
        data["name"] = data["name"]
        collection.insert_one(data)
        return jsonify({"response": "User created"})
    except Exception as e:
        print(e)
        return jsonify({"response": "Invalid request"}), 400

def sign_in(data):
    try:
        db = access_db()
        collection = db["User"]
        if "user_name" in data.keys():
            user_name = "user_name"
        else:
            user_name = "e_mail"
        user = collection.find_one({user_name: data[user_name]})
        print(hash(data["password"]))
        if not user or user["password"] != get_hash_value(data["password"]):
            return jsonify({"response": "Username/Password incorrect"}), 401
        token = create_access_token(identity=user["_id"], fresh=True)
        return jsonify({"token": token}), 200
    except Exception as e:
        print(e)
        return jsonify({"response": "Invalid request"}), 400

def user_delete():
    user = get_jwt_identity()
    db = access_db()
    notes = db["Note"]
    users = db["User"]
    notes.delete_many({"user": user})
    user = users.delete_one({"_id": user})
    return jsonify({"response": "User deleted successfully"})

def show_users():
    db = access_db()
    collection = db["User"]
    docs = []
    for doc in collection.find():
        try:
            doc["password"] = str(doc["password"])
        except:
            pass
        docs.append(doc)
    return jsonify(docs)

def is_admin(user):
    collection = access_db()["User"]
    result = collection.find_one({"_id": user})
    return result["is_admin"]

def admin_delete(user_name):
    user = get_jwt_identity()
    if not is_admin(user):
        return jsonify({"response": "Unauthorized action"}), 401
    collection =  access_db()["User"]
    result = collection.find_one({"user_name": user_name})
    if not result:
        return jsonify({"response": "User not found"})
    collection.delete_one({"_id": result["_id"]})
    return jsonify({"response": "User deleted successfully"})

def admin_add(data):
    user = get_jwt_identity()
    if not is_admin(user):
        return jsonify({"response": "Unauthorized action"}), 401
    collection =  access_db()["User"]
    try:
        data["user_name"] = data["user_name"]
        data["e_mail"] = data["e_mail"]
        data["is_admin"] = True
        data["password"] = get_hash_value(data["password"])
        data["_id"] = uuid.uuid4().hex
        data["name"] = data["name"]
        if collection.find_one({"user_name": data["user_name"]}):
             return jsonify({"response": "user name already exists"}), 409
        if collection.find_one({"e_mail": data["e_mail"]}):
             return jsonify({"response": "email already exists"}), 409
        collection.insert_one(data)
        return jsonify({"response": "Admin user created"})
        
    except Exception as e:
        print(e)
        return jsonify({"response": "Invalid request"}), 400