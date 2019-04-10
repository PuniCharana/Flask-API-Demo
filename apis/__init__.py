from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://punicharana:password@localhost:5432/template1'
db.init_app(app)

from apis.v1 import blueprint as blueprint_v1
from apis.v2 import blueprint as blueprint_v2
app.register_blueprint(blueprint_v1)
app.register_blueprint(blueprint_v2)