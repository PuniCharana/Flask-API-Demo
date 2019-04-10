from flask_restplus import Namespace, Resource, fields

api = Namespace('bars', description='Bars related operations')

bar = api.model('Bar', {
    'id': fields.String(required=True, description='The bar identifier'),
    'name': fields.String(required=True, description='The bar name'),
})

BARS = [
    {'id': 'felix', 'name': 'Felix'},
]


@api.route('/')
class barList(Resource):
    @api.doc('list_bars')
    @api.marshal_list_with(bar)
    def get(self):
        '''List all bars'''
        return BARS


@api.route('/<id>')
@api.param('id', 'The bar identifier')
@api.response(404, 'bar not found')
class Bar(Resource):
    @api.doc('get_bar')
    @api.marshal_with(bar)
    def get(self, id):
        '''Fetch a bar given its identifier'''
        for bar in BARS:
            if bar['id'] == id:
                return bar
        api.abort(404)