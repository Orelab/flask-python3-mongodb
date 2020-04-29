from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name="you")

@app.route('/messages', methods=['POST', 'GET'])
def messages():
    if request.method == 'POST':
        return 'saved'
    else:
        return 'messages here'






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