from django.db import models

# Create your models here.
class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number} {self.street}, {self.city}, {self.state}"

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name