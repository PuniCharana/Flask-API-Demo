from .models import Cat

def get_all_cats():
    return Cat.query.all()

def  add_new_cat():
    return True

def get_cat_by_id(cat_id):
    return Cat.query.filter_by(id=cat_id).first()