from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Reset a user's password"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str, nargs="?", default="password123")

    def handle(self, *args, **options):
        user = User.objects.filter(username=options["username"]).first()
        if not user:
            self.stderr.write(self.style.ERROR(f'User "{options["username"]}" not found'))
            return
        user.set_password(options["password"])
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Password for "{options["username"]}" reset to "{options["password"]}"'))
