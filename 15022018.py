from flask import Flask,request,jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "aman",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "pawan",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "pankaj",
        "age": 22,
        "occupation": "Web Developer"
    }
]

# endpoint to show user
@app.route("/user/<string:name>", methods=["GET"])
def get_user(name):
    for user in users:
        if (name == user["name"]):
            return jsonify(user)
    return "User not found"

# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    name = request.json['name']
    age = request.json['age']
    occupation=request.json['occupation']
    for user in users:
        if(name==user['name']):
            return "User with name {} already exists".format(name)

    user = {
        "name": name,
        "age": age,
        "occupation": occupation
    }
    users.append(user)
    return jsonify(user)

# endpoint to update user
@app.route("/user", methods=["PUT"])
def user_update():
    name = request.json['name']
    age = request.json['age']
    occupation = request.json['occupation']

    for user in users:
        if (name == user["name"]):
            user["age"] = age
            user["occupation"] = occupation
            return jsonify(user)

    user = {
        "name": name,
        "age": age,
        "occupation": occupation
    }
    users.append(user)
    return jsonify(user)

# endpoint to delete user
@app.route("/user/<string:name>", methods=["DELETE"])
def user_delete(name):
    for user in users:
        if (name == user["name"]):
            users.remove(user)
            return "{} is deleted.".format(name)
    return "User {} does not exists".format(name)

if __name__ == '__main__':
    app.run(debug=True)
