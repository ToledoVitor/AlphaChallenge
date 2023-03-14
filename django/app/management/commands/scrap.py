from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)

from app.scrapper import ScrapperClient


class Command(BaseCommand):
    help = 'Starts the ScrapperClient and updates the database'

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        try:
            self.stdout.write(
                self.style.WARNING(
                    'Starting scrapper client. This process can take some time'
                )
            )
            client = ScrapperClient()
            client.scrap()
        except Exception as e:
            raise CommandError(e)
        else:
            self.stdout.write(
                self.style.SUCCESS('Scrapper run successfully. Models updated')
            )
