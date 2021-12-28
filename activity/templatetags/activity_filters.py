from django import template

register = template.Library()

@register.filter(name='pricequantity')
def pricequantity(value, arg):
    return value * arg
