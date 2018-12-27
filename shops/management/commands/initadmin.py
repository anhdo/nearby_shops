from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(
                username="admin",
                password="admin",
                email="admin@example.com",
            ).save()
        except:
            pass
