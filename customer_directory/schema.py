import graphene
from graphene_django import DjangoObjectType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    people = graphene.List(PersonType, page=graphene.Int(), page_size=graphene.Int())

    def resolve_people(root, info, page=None, page_size=None):
        queryset = Person.objects.all()

        if page is not None and page_size is not None:
            paginator = Paginator(queryset, page_size)
            try:
                people_page = paginator.page(page)
            except (PageNotAnInteger, EmptyPage):
                # Handle invalid page number or empty page
                return []
            return people_page
        else:
            return queryset

schema = graphene.Schema(query=Query)