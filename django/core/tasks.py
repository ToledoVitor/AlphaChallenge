from celery import shared_task
from django.core.management import call_command


@shared_task
def scrap():
    call_command(
        'scrap',
    )


@shared_task
def check_price_alerts():
    call_command(
        'check_price_alerts',
    )
