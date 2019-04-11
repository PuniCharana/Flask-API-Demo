from flask import request
from flask_restplus import Namespace, Resource, fields

from .business import get_all_cats, get_cat_by_id, add_new_cat
from .models import CatSchema

ns = Namespace('cats', description='Cats related operations')

cat = ns.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})


@ns.route('/')
class CatList(Resource):
    @ns.doc('list_cats')
    @ns.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        cat_schema = CatSchema(many=True)
        result = get_all_cats()
        return result

    def post(self):
        '''Add new cat'''
        cat_schema = CatSchema(many=True)
        json_input = request.get_json()
        data, errors = cat_schema.load(json_input)
        if errors:
            print(errors)
            return errors
            # return jsonify({'errors': errors}), 422

        print(data)

        return add_new_cat()


@ns.route('/<id>')
@ns.param('id', 'The cat identifier')
# @ns.response(404, 'Cat not found')
class Cat(Resource):
    @ns.doc('get_cat')
    @ns.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        cat_schema = CatSchema(dump_only=('id'))
        result = get_cat_by_id(id)

        if result:
            return result, 200

        ns.abort(404, error="stfu")
