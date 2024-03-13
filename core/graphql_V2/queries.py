import graphene


class Query(graphene.ObjectType):

    #Category
    category = graphene.Field(RetrieveCategoryType, id=graphene.ID(required=True))
    all_categories = graphene.List(CategoryType)

    def resolve_category(self, info, id):
        return Category.objects.get(id=id)

    def resolve_all_categories(self, info):
        return Category.objects.all()