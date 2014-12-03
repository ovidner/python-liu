from django.core.management.base import BaseCommand, CommandError

from liu.django.models import LiUID

class Command(BaseCommand):
    def handle(self, *args, **options):
        LiUID.objects.all().fetch()