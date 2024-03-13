from graphene import List, String, ObjectType
from graphene_django.types import DjangoObjectType
from ecommerce.models import Category, Material, Type


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['name']

class RetrieveMaterialType(DjangoObjectType):
    class Meta:
        model = Material
        fields = ['name', 'description']

class RetrieveCategoryType(DjangoObjectType):
    materials = List(RetrieveMaterialType)
    class Meta:
        model = Category
        fields = ['name', 'description', 'material']

    def resolve_materials(self, info):
        return self.materials.all()


class MaterialType(DjangoObjectType):

    custom_field = String()
    custom_array = List(String)
    class Meta:
        model = Material
        fields = ['category', 'name', 'description', 'custom_field', 'custom_array']

    def resolve_custom_field(self, info):
        return f"{self.category.name} - {self.name}"

    def resolve_custom_array(self, info):
        return [self.category.name]

class TypeType(DjangoObjectType):
    class Meta:
        model = Type
        fields = ['name', 'category']
