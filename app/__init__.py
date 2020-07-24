from flask import Flask

app = Flask(__name__, static_folder='static/data', template_folder='templates')

app.config['UPLOAD_FOLDER'] = 'static/data'

from app import views

