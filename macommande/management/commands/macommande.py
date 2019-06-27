import os 

from django.core.management.base import BaseCommand
from sentry_sdk import capture_message


class Command(BaseCommand):
    def handle(self, *args, **options):
        capture_message(
            "macommande called, IMMOFAKE has value "
            f"{os.environ.get('IMMOFAKE', 'no value')}"
        )
