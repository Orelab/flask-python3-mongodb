from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape
from flask_pymongo import PyMongo
import datetime
import sys

# https://stackoverflow.com/questions/46752051/flask-pymongo-string-back-to-objectid
# https://pymongo.readthedocs.io/en/stable/tutorial.html
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

# https://flask-pymongo.readthedocs.io/en/latest/
app.config["MONGO_URI"] = "mongodb://localhost:27017/pyflask"
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html', name="you")


@app.route('/messages', methods=['POST', 'GET'])
def messages():
    messages = mongo.db.messages.find({})
    # https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
    return render_template('messages.html', name="you", messages=messages if messages.count() else False)


@app.route("/api/messages")
def api_messages():
    """
    API style :)
    (not used here, but very cool)
    """
    return mongo.db.messages.find({})


@app.route("/api/messages/save", methods=["POST"])
def api_messages_save():

    message = {
        "date": datetime.datetime.now(),
        "text": request.form["message"],
        "done": False
    }

    mongo.db.messages.insert_one(message)
    return redirect(url_for("messages"))


@app.route("/api/messages/delete", methods=["POST"])
def api_messages_delete():
    _id = request.form["id"]

    mongo.db.messages.delete_one({'_id': ObjectId(_id)})
    return redirect(url_for("messages"))


@app.route("/api/messages/done", methods=["POST"])
def api_messages_done():
    _id = request.form["id"]

    if "done" in request.form:
        done = request.form["done"]
    else:
        done = False

    mongo.db.messages.update_one({'_id': ObjectId(_id)}, {"$set":{"done":done=="on"}} )
    return redirect(url_for("messages"))





# @app.route('/user/<username>')
# def user(username):
#     return 'User %s' % escape(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return 'Subpath %s' % escape(subpath)




# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('hello'))
#     print(url_for('hello', next='/'))
#     print(url_for('user', username='John Doe'))
#     print(url_for('static', filename='style.css'))


# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'