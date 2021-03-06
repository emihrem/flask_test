from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/index')
def index_page():
    return 'Index page'

@app.route('/<name>')
def hello(name):
    return f'Hello, {escape(name)}!'

if __name__ == '__main__':
    app.run()