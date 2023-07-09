import graphene
from graphene_django import DjangoObjectType

from view_customers.models import Person

class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("id", "name", "email")

class Query(graphene.ObjectType):
    people = graphene.List(PersonType)
    
    def resolve_people(root, info):
        # We can easily optimize query count in the resolve method
        return Person.objects.all()    

schema = graphene.Schema(query=Query)