from flask_restplus import Api
from flask import Blueprint
from .ns_bar import api as bar
from .ns_foo import api as foo

blueprint = Blueprint('Version 2', __name__, url_prefix='/v2')

api = Api(blueprint,
    title='Version 2',
    version='1.0',
    description='A description',
    # All API metadatas
)
api.add_namespace(bar)
api.add_namespace(foo)