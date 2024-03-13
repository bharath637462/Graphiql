from graphene import List, String, ObjectType
from graphene_django.types import DjangoObjectType


class CategoryType(DjangoObjectType):
    class Meta:
        model = ''
        fields = ['name']