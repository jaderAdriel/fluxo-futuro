from django.db import models

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('IN', 'Entrada'),
        ('OUT', 'Saída'),
    ]

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    def __str__(self):
        return f'{self.description} - {self.amount}'

