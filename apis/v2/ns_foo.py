from flask_restplus import Namespace, Resource, fields

api = Namespace('foos', description='Foos related operations')

foo = api.model('Foo', {
    'id': fields.String(required=True, description='The foo identifier'),
    'name': fields.String(required=True, description='The foo name'),
})

FOOS = [
    {'id': 'felix', 'name': 'Felix'},
]


@api.route('/')
class fooList(Resource):
    @api.doc('list_foos')
    @api.marshal_list_with(foo)
    def get(self):
        '''List all foos'''
        return FOOS


@api.route('/<id>')
@api.param('id', 'The foo identifier')
@api.response(404, 'foo not found')
class foo(Resource):
    @api.doc('get_foo')
    @api.marshal_with(foo)
    def get(self, id):
        '''Fetch a foo given its identifier'''
        for foo in FOOS:
            if foo['id'] == id:
                return foo
        api.abort(404)