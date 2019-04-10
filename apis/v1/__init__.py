from flask_restplus import Api
from flask import Blueprint
from .cat import api as ns1
from .dog import api as ns2

blueprint = Blueprint('Version 1', __name__, url_prefix='/v1')

api = Api(blueprint,
    title='Version 1',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1)
api.add_namespace(ns2)