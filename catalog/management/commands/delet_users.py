from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Delete users"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='+', type=int, help='Enter a number from 1')

    def handle(self, *args, **kwargs):
        users = kwargs['some_id']
        a = User.objects.filter(pk=users[0])
        print(a)

