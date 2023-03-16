from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)
from django.core.mail import mail_admins

from app.models import AvisoPreco, Cotacao


class Command(BaseCommand):
    help = 'Check for all prices alerts, and if matches the condition, informs the user'

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        try:
            self.stdout.write(
                self.style.WARNING(
                    'Starting checking. This proccess can take some time'
                )
            )
            for aviso in AvisoPreco.objects.filter(completed=False):
                last_update = (
                    Cotacao.objects.order_by('-updated_at')
                    .filter(code=aviso.cotacao_code)
                    .first()
                )

                if last_update.last_price < aviso.value:
                    aviso.completed = True
                    aviso.save()

                    message = (
                        'Olá, \n'
                        'Nosso sistema atualizou os valores das cotações, e '
                        f'parece que seu aviso de preço para o ativo {aviso.cotacao_code}'
                        'chegou ao preço desejado! \n \n'
                        'Acesse nosso site e confira os preços atuais.'
                    )
                    mail_subject = f'Aviso de Preço para {aviso.cotacao_code}'
                    mail_admins(
                        subject=mail_subject,
                        message=message,
                        html_message=None,
                    )
        except Exception as e:
            raise CommandError(e)
        else:
            self.stdout.write(self.style.SUCCESS('Email alerts sent.'))
