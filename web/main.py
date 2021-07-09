import os

from flask import Flask, jsonify, request
from peewee import Model, CharField
from playhouse.db_url import connect

app = Flask(__name__)

db = connect(os.environ["MYSQL_URL"])


class BaseModel(Model):
    class Meta:
        database = db


class Account(BaseModel):
    username = CharField(unique=True)


with db:
    db.create_tables([Account])


@app.route("/health")
def health():
    return jsonify(state="up")


@app.route("/v1/accounts", methods=["POST"])
def create():
    parameters = request.get_json()
    account = Account(**parameters)
    account.save()
    return jsonify({
        "id": account.id,
        "username": account.username
    }), 201


@app.route("/v1/accounts/<id>", methods=["GET"])
def find(id):
    account = Account.get((Account.id == id))
    return jsonify({
        "id": account.id,
        "username": account.username
    })


@app.route("/v1/accounts/<id>", methods=["DELETE"])
def delete(id):
    Account.delete_by_id(id)
    return "", 204


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
