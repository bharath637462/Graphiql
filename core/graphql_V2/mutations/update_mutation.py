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