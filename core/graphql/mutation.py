import graphene

from core.graphql.types import CategoryType
from ecommerce.models import Category, Material


class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, description=None):
        category = Category(name=name, description=description)
        category.save()
        return CreateCategoryMutation(category=category)


# Mutation for updating an existing category
class UpdateCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, id, name=None, description=None):
        category = Category.objects.get(id=id)
        if name is not None:
            category.name = name
        if description is not None:
            category.description = description
        category.save()
        return UpdateCategoryMutation(category=category)

# Mutation for deleting a category
class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            Category.objects.get(id=id).delete()
            success = True
        except Category.DoesNotExist:
            success = False
        return DeleteCategoryMutation(success=success)


class CreateMaterialMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, description=None):
        material = Material(name=name, description=description)
        material.save()
        return CreateMaterialMutation(material=material)


# Create the Mutation class
class Mutation(graphene.ObjectType):

    # Category
    create_category = CreateCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()

    # Material
    create_material = CreateMaterialMutation.Field()
