import graphene

from core.graphql.mutation import Mutation
from core.graphql.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
