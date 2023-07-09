import graphene
from graphene_django import DjangoObjectType

from view_customers.models import Person, Address

class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        fields = ("id", "number", "street", "city", "state")

class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("id", "name", "email")
    address = graphene.Field(AddressType)

class Query(graphene.ObjectType):
    people = graphene.List(PersonType)
    
    def resolve_people(root, info):
        # We can easily optimize query count in the resolve method
        return Person.objects.all()    

schema = graphene.Schema(query=Query)