import graphene

from core.graphql.types import RetrieveCategoryType, CategoryType, MaterialType, TypeType
from ecommerce.models import Category, Material, Type


class Query(graphene.ObjectType):

    #Category
    category = graphene.Field(RetrieveCategoryType, id=graphene.ID(required=True))
    all_categories = graphene.List(CategoryType)

    def resolve_category(self, info, id):
        return Category.objects.get(id=id)

    def resolve_all_categories(self, info):
        return Category.objects.all()


    #Material
    material = graphene.Field(MaterialType, id=graphene.ID(required=True))
    all_materials = graphene.List(MaterialType)

    def resolve_material(self, info, id):
        return Material.objects.get(id=id)

    def resolve_all_materials(self, info):
        return Material.objects.all()

    #types
    type = graphene.Field(TypeType, id=graphene.ID(required=True))
    all_types = graphene.List(TypeType)

    def resolve_type(self, info, id):
        return Type.objects.get(id=id)

    def resolve_all_types(self, info):
        return Type.objects.all()



