from django_graphbox.builder import SchemaBuilder
from .models import Category

builder = SchemaBuilder()
builder.add_model(Category)

query_class = builder.build_schema_query()
mutation_class = builder.build_schema_mutation()