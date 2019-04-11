from marshmallow import Schema

from apis import db


class Cat(db.Model):
    __tablename__ = 'cat'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class CatSchema(Schema):
    class Meta:
        model = Cat
        fields = ('id', 'name')
