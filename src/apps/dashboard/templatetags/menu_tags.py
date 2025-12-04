from django import template

register = template.Library()

# Essa função verifica se a url atual contém o nome da url passada como parâmetro
@register.simple_tag(takes_context=True)
def activeMenu(context, url_name):
    try:
        if url_name in context['request'].resolver_match.url_name:
            return 'active bg-gradient-dark text-white'
    except:
        pass
    return 'text-dark'