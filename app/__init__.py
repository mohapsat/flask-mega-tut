from flask import Flask

app = Flask(__name__)
app.config.from_object('config') # call config.py with configurations

from app import views # import views from the app package