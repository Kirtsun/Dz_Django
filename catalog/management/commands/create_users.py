from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "init"

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        pass
