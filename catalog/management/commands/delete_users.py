from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Create random users"

    def add_arguments(self, parser):
        parser.add_argument('some_id', type=int, choices=range(1, 11), help='')

    def handle(self, *args, **kwargs):