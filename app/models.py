from django.db import models


class Ativo(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)

    last_evaluation = models.CharField(max_length=10)
    last_day_evaluation = models.CharField(max_length=10)
    variation = models.CharField(max_length=10)

    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["updated_at"]
        verbose_name = "Ativo"
        verbose_name_plural = "Ativos"

    def __str__(self):
        return f"{self.name} - {self.code}"
