PERMISSION_TRANSLATED = {
    #modelos do sistema traduzidos 
    'department': 'Departamentos',
    'event': 'Eventos',
    'financial': 'Financeiro',
    
    # Actions
    'add': 'Adicionar',
    'change': 'Alterar',
    'delete': 'Excluir',
    'view': 'Visualizar',
}

def translate_permission(permission):
    """função utilitária para traduzir permissões do django para português brasileiro"""
    #mapeamento das ações em inglês do django para chaves simplificadas
    action_map = {
        'can add': 'add',
        'can change': 'change', 
        'can delete': 'delete',
        'can view': 'view'
    }
    
    #identifica qual ação está sendo usada na permissão
    action_key = None
    for key, value in action_map.items():
        if permission.name.lower().startswith(key):
            action_key = value
            break
    
    #se encontrou uma ação válida, constrói a tradução completa
    if action_key:
        #busca a tradução do modelo no dicionário ou usa o nome original
        modelo_traduzido = PERMISSION_TRANSLATED.get(permission.content_type.model, permission.content_type.model)
        #busca a tradução da ação no dicionário ou usa a chave original
        acao_traduzida = PERMISSION_TRANSLATED.get(action_key, action_key)
        #retorna no formato "modelo - ação"
        return f"{modelo_traduzido} - {acao_traduzida}"
    
    #caso não encontre uma ação mapeada, retorna tradução básica do modelo
    return f"{PERMISSION_TRANSLATED.get(permission.content_type.model, permission.content_type.model)} - {permission.name}"