from flask_restplus import Namespace, Resource, fields
from .business import get_all_cats, get_cat_by_id, add_new_cat
from .models import CatSchema
api = Namespace('cats', description='Cats related operations')

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        cat_schema = CatSchema(many=True)
        result = get_all_cats()
        return result

    def post(self):
        '''Add new cat'''
        return add_new_cat()


@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        cat_schema = CatSchema(dump_only=('id'))
        result = get_cat_by_id(id)
        return result, 200