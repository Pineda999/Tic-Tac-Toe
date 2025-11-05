from django import template
register = template.Library()

@register.filter
def index(lista, i):
    return lista[i]