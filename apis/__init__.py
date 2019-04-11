from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.exc import ProgrammingError

from settings import Config

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)
app.config.from_object(Config)
db.init_app(app)

from apis.v1 import blueprint as blueprint_v1
from apis.v2 import blueprint as blueprint_v2

app.register_blueprint(blueprint_v1)
app.register_blueprint(blueprint_v2)


@app.errorhandler(ProgrammingError)
def programming_error(error):
    print(error)
    return 'ProgrammingError', 400


@app.errorhandler(500)
def error_500(error):
    print(error)
    return '500', 400


@app.errorhandler(Exception)
def alc_error(error):
    print(error)
    return 'Exception', 400


@app.errorhandler(exc.IntegrityError)
def db_constraint_error(error):
    print("IntegrityError")
    print(error)
    return "IntegrityError", 400


@app.errorhandler(exc.NoForeignKeysError)
def db_no_foreign_key_error(error):
    print(error)
    return "NoForeignKeysError", 400


@app.errorhandler(exc.NoReferenceError)
def db_no_reference_error(error):
    print(error)
    return "NoReferenceError", 400


@app.errorhandler(exc.NoReferencedColumnError)
def db_no_reference_column_error(error):
    print(error)
    return "NoReferencedColumnError", 400


@app.errorhandler(exc.NoReferencedTableError)
def db_no_reference_table_error(error):
    print(error)
    return "NoReferencedTableError", 400


@app.errorhandler(exc.NoSuchColumnError)
def db_no_such_column_error(error):
    print(error)
    return "NoSuchColumnError", 400


@app.errorhandler(exc.NoSuchTableError)
def db_no_such_table_error(error):
    print(error)
    return "NoSuchTableError", 400


@app.errorhandler(exc.ProgrammingError)
def db_programming_error(error):
    print(error)
    return "ProgrammingError", 400


@app.errorhandler(exc.StatementError)
def db_statement_error(error):
    print(error)
    return "StatementError", 400


@app.errorhandler(exc.TimeoutError)
def db_timeout_error(error):
    print(error)
    return "TimeoutError", 504


@app.errorhandler(exc.InvalidRequestError)
def invalid_request_error(error):
    print(error)
    return "InvalidRequestError", 504


@app.errorhandler(AttributeError)
def attribute_error(error):
    print(error)
    return "AttributeError", 500


@app.errorhandler(KeyError)
def attribute_error(error):
    print(error)
    return "KeyError", 500
