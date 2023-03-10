from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('users', nargs=1, type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        user = []
        for _ in range(int(options['users'][0])):
            user.append(User(username=fake.name(), email=fake.email(), password=make_password(fake.password())))
        User.objects.bulk_create(user)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {options["users"][0]} user(s)'))
