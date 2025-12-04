from django.db import models


class Management(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        blank=False, 
        null=False,
        verbose_name="Nome da gestão"
    )

    begin_date = models.DateField(
        blank=False, 
        null=False,
        verbose_name="Início mandato"
    )

    end_date = models.DateField(
        blank=False, 
        null=False,
        verbose_name="Fim mandato"
    )

    class Meta:
        ordering = ["-begin_date"]  # ordena por mais recente
        verbose_name = "Gestão"
        verbose_name_plural = "Gestões"

    def __str__(self):
        return f"{self.name} ({self.begin_date} → {self.end_date})"