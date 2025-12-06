from django.db import models

class Meeting(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="Título da reunião"
    )

    date = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name="Data e hora"
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Local"
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Pauta / Descrição"
    )

    class Meta:
        ordering = ["-date"]
        verbose_name = "Reunião"
        verbose_name_plural = "Reuniões"

    def __str__(self):
        return f"{self.title} ({self.date})"
