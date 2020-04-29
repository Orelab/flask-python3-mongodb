from flask import Flask, url_for, request, render_template
from markupsafe import escape
from flask_pymongo import PyMongo



app = Flask(__name__)

# https://flask-pymongo.readthedocs.io/en/latest/
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html', name="you")

@app.route('/messages', methods=['POST', 'GET'])
def messages():
    if request.method == 'POST':
        return 'saved'
    else:
        return render_template('messages.html', name="you")


@app.route("/api/messages")
def api_messages():
    # user = get_current_user()
    online_users = mongo.db.users.find({"online": True})
    user = {
        "username": "Ford",
        "theme": "Mustang"
    }
    return {
        "username": user["username"],
        "theme": user["theme"],
    }



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