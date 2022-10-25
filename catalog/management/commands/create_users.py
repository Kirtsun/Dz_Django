from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import User

fake = Faker()


class Command(BaseCommand):
    help = "init"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='+', type=int, choises=range(1, 10))

    def handle(self, *args, **options):
        some_id = options['some_id']
        for i in range(some_id):
            try:
                some_id <= 10
            except ValueError:
                self.stdout.write('invalid value')
            User.objects.create(username=fake.username(), email=fake.email(), password=fake.password())


