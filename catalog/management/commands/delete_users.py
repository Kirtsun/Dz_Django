from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Delete users"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='+', type=int, help='Enter a number from 1')

    def handle(self, *args, **kwargs):
        users = kwargs['some_id']
        a = User.objects.filter(id__in=users)
        b = User.objects.filter(id__in=users, is_superuser=True).exists()
        if b is True:
            self.stdout.write(f"Unable to delete super user, enter other id!")
        else:
            a.delete()
            self.stdout.write(f'Users deleted with success!')





