from django.test import TestCase
from graphene.test import Client
from .schema import schema

class GraphQLTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_basic_query(self):
        query = '''
        query basicQuery {
            people {
                email
                name
                address {
                    number
                    street
                    city
                    state
                }
            }
        }
        '''
        executed = self.client.execute(query)
        response = executed['data']['people']
        self.assertEqual(len(response), 2) 
        person = response[0]
        self.assertIn('email', person)
        self.assertIn('name', person)
        self.assertIn('address', person)
        address = person['address']
        self.assertIn('number', address)
        self.assertIn('street', address)
        self.assertIn('city', address)
        self.assertIn('state', address)
