from flask import Flask, render_template
from os import environ
from map_views import map_app
from editor_views import editor_app
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.register_blueprint(map_app)
app.register_blueprint(editor_app)