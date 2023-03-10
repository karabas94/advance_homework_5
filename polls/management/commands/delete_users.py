from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Delete users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        users = options['user_ids']
        if User.objects.filter(id__in=users, is_superuser=True):
            raise CommandError('Cannot delete superuser')
        else:
            User.objects.filter(id__in=users, is_superuser=False).delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted user(s) with id number {", ".join(map(str, users))}'))
