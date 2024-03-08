from django.core.management.base import BaseCommand
from kuznia.all.management.commands.bot import start

class Command(BaseCommand):
    help = 'ТГ'

    def handle(self, *args, **options):
        # Your command logic here
        start()