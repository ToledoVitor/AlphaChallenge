# Generated by Django 4.1.7 on 2023-03-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Ativo',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'table',
                    models.CharField(
                        choices=[
                            ('Cotacões Intradia', 'cotacoes-intradia'),
                            ('BDRs mais negociados', 'bdrs-mais-negociados'),
                            ('Fundos Imobiliários', 'fundos-imobiliarios'),
                        ],
                        max_length=20,
                    ),
                ),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=5)),
                (
                    'last_price',
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    'last_day_price',
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    'variation',
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ativo',
                'verbose_name_plural': 'Ativos',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='AvisoPreco',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('ativo_code', models.CharField(max_length=5)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]