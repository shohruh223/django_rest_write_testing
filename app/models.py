from django.db.models import Model, DateTimeField, CharField, ForeignKey, SET_NULL, TextField, DecimalField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = CharField(max_length=155, unique=True)


class Product(BaseModel):
    category = ForeignKey(Category, SET_NULL, null=True, related_name='categories')
    name = CharField(max_length=155)
    description = TextField()
    price = DecimalField(max_digits=20, decimal_places=2)