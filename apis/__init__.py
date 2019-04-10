from flask import Flask

from apis.v1 import blueprint as blueprint_v1
from apis.v2 import blueprint as blueprint_v2

app = Flask(__name__)
app.register_blueprint(blueprint_v1)
app.register_blueprint(blueprint_v2)