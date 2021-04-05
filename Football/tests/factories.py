import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class SuperUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('test'))
    is_staff = True
    is_superuser = True
