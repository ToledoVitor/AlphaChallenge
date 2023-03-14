from django.db import models


def Ativos(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)

    last_evaluation = models.DecimalField(decimal_places=2)
    last_day_evaluation = models.DecimalField(decimal_places=2)
    variation = models.DecimalField(decimal_places=2)

    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        ordering = ["updated_at"]
        verbose_name = "Ativos"
        verbose_name_plural = "Ativos"

    def __str__(self):
        return f"{self.name} - {self.code}"
