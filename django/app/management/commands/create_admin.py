from django.contrib.auth.models import User
from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)


class Command(BaseCommand):
    help = 'Create default admin user'

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        if User.objects.exists():
            # No need to create new user, the project was already running
            return

        try:
            self.stdout.write(
                self.style.WARNING(
                    'Creating superuser'
                )
            )
            User.objects.create_superuser(
                username='admin', email='admin@mail.com', password='admin'
            )
        except Exception as e:
            raise CommandError(e)
        else:
            self.stdout.write(self.style.SUCCESS('Superuser created.'))
