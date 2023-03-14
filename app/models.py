from django.db import models


class Ativo(models.Model):
    TABLE_CHOICHES = (
        ("Cotacões Intradia", "cotacoes-intradia"),
        ("BDRs mais negociados", "bdrs-mais-negociados"),
        ("Fundos Imobiliários", "fundos-imobiliarios"),
    )

    table = models.CharField(
        choices=TABLE_CHOICHES, max_length=20, blank=False, null=False
    )
    name = models.CharField(max_length=30, blank=False, null=False)
    code = models.CharField(max_length=5, blank=False, null=False)

    last_evaluation = models.CharField(max_length=10, blank=True, null=True)
    last_day_evaluation = models.CharField(max_length=10, blank=True, null=True)
    variation = models.CharField(max_length=10, blank=True, null=True)

    updated_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    class Meta:
        ordering = ["updated_at"]
        verbose_name = "Ativo"
        verbose_name_plural = "Ativos"

    def pretty_updated_at(self):
        return self.updated_at.strftime("%H:%M %d/%m/%Y")

    def __str__(self):
        return f"{self.name} - {self.code}"
