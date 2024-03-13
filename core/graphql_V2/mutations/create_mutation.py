class CreateMaterialMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, description=None):
        material = Material(name=name, description=description)
        material.save()
        return CreateMaterialMutation(material=material)