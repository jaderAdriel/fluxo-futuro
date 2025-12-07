from django.db import models
from django.contrib.auth.models import User, Group


class Department(Group):

    members = models.ManyToManyField(
        User, 
        blank=True, 
        related_name='member_department', 
        verbose_name="Membros"
    )

    is_active = models.BooleanField(
        null=False,
        default=True, 
        verbose_name="Ativo"
    )

    created_by = models.ForeignKey(
        User, 
        blank=False,
        null=True, 
        on_delete=models.SET_NULL,
        related_name="department_creator",
        verbose_name="Criado por", 
    )

    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Atualizado em"
    )

    created_at = models.DateField(
        auto_now_add=True, 
        editable=False,
        verbose_name="Criado em"
    )

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f"{self.name}"