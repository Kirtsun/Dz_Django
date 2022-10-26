from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from django.contrib.auth import get_user_model

from faker import Faker

User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    help = "Create random users"

    def add_arguments(self, parser):
        parser.add_argument('some_id', type=int, choices=range(1, 11), help='Enter a number from 1 to 10 to'
                                                                            ' create random users')

    def handle(self, *args, **kwargs):
        objs = []
        total = kwargs['some_id']
        for i in range(total):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()

            k = User(
                username=username,
                email=email,
                password=make_password(password),
            )
            objs.append(k)
        User.objects.bulk_create(objs)
