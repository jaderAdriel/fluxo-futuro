from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Department


@receiver(post_save, sender=Department)
def department_post_save(sender, instance, created, **kwargs):
    """
    Signal executado após salvar um departamento.
    Garante que o department seja também salvo como um grupo na tabela auth_group.
    """
    
    atualizar_usuarios_no_grupo(instance)


@receiver(m2m_changed, sender=Department.members.through)
def department_membro_changed(sender, instance, action, pk_set, **kwargs):
    """
    Signal executado quando os membros de um department são alterados.
    Automaticamente adiciona/remove usuários do grupo correspondente.
    """
    if action == "post_add":
        #Usuários foram adicionados ao department
        if pk_set:
            usuarios = User.objects.filter(pk__in=pk_set)
            for usuario in usuarios:
                #Adiciona o usuário ao grupo (department)
                usuario.groups.add(instance)
    
    elif action == "post_remove":
        #Usuários foram removidos do department
        if pk_set:
            usuarios = User.objects.filter(pk__in=pk_set)
            for usuario in usuarios:
                #Remove o usuário do grupo (department)
                usuario.groups.remove(instance)
    
    elif action == "post_clear":
        #Todos os membros foram removidos do department
        #Remove todos os usuários do grupo
        for usuario in instance.user_set.all():
            usuario.groups.remove(instance)


def atualizar_usuarios_no_grupo(department: Department):
    """
    Função auxiliar para sincronizar os membros do department com o grupo.
    Garante que todos os usuários definidos como membros do department
    estejam também no grupo correspondente.
    """
    #Obter todos os usuários que deveriam estar no grupo
    membros_department = department.members.all()
    
    #Obter todos os usuários que estão atualmente no grupo
    usuarios_no_grupo = department.user_set.all()
    
    #Adicionar usuários que estão no department mas não no grupo
    for usuario in membros_department:
        if usuario not in usuarios_no_grupo:
            usuario.groups.add(department)
    
    #Remover usuários que estão no grupo mas não no department
    for usuario in usuarios_no_grupo:
        if usuario not in membros_department:
            usuario.groups.remove(department)

