from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
@app.route('/hw')
def hello_world():
    return 'Hello, World!'
# to run  flask app 
#PS $env:FLASK_APP = "app.py"
#PS python -m flask run
#enabling debug and devmode
#PS $env:FLASK_ENV="development"
#PS  $env:FLASK_DEBUG="1"