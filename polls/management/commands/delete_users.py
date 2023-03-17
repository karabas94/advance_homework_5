from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

User = get_user_model()


class Command(BaseCommand):
    help = 'Delete users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        users = options['user_ids']
        if User.objects.filter(id__in=users, is_superuser=True).exists():
            raise CommandError('Cannot delete superuser')
        else:
            User.objects.filter(id__in=users, is_superuser=False).delete()

        self.stdout.write(
            self.style.SUCCESS(f'Successfully deleted user(s) with id number {", ".join(map(str, users))}'))
