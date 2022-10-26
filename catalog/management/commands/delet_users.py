from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Create random users"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='+', type=int, help='Enter a number from 1 to 10 to create random users')

    def handle(self, *args, **kwargs):
        users = kwargs['some_id']

        for i in users:
            try:
                user = User.objects.get(pk=i)
                user.delete()
                self.stdout.write('User "%s (%s)" deleted with success!' % (user.username, i))
            except User.DoesNotExist:
                self.stdout.write('User with id "%s" does not exist.' % i)