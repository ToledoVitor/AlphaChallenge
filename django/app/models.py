from django.db import models


class Cotacao(models.Model):
    TABLE_CHOICHES = (
        ('Cotacões Intradia', 'cotacoes-intradia'),
        ('BDRs mais negociados', 'bdrs-mais-negociados'),
        ('Fundos Imobiliários', 'fundos-imobiliarios'),
    )

    table = models.CharField(
        verbose_name='Tabela Referência',
        choices=TABLE_CHOICHES,
        max_length=20,
        blank=False,
        null=False,
    )
    name = models.CharField(
        verbose_name='Nome do Ativo', max_length=100, blank=False, null=False
    )
    code = models.CharField(
        verbose_name='Código do Ativo', max_length=10, blank=False, null=False
    )

    last_price = models.DecimalField(
        verbose_name='Último Preço do Ativo',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    last_day_price = models.DecimalField(
        verbose_name='Preço do Último Dia',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    variation = models.DecimalField(
        verbose_name='Variação',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='Atualizado em',
        auto_now_add=True,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['updated_at']
        verbose_name = 'Cotação'
        verbose_name_plural = 'Cotações'

    def pretty_updated_at(self):
        return self.updated_at.strftime('%H:%M %d/%m/%Y')

    def __str__(self):
        return f'{self.name} - {self.code}'


class AvisoPreco(models.Model):
    cotacao_code = models.CharField(
        verbose_name='Código do Ativo', max_length=10, blank=False, null=False
    )
    value = models.DecimalField(
        verbose_name='Preço Alvo', max_digits=10, decimal_places=2
    )

    # If true, the user was already warned about the price
    completed = models.BooleanField(default=False)
