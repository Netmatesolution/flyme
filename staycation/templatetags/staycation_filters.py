from django import template

register = template.Library()

@register.filter(name='pagination')
def lower(value,arg):
    # current_page = int(value[-1])
    # page = arg
    print(value,arg)
    if(value==''):
        value=1
    if(int(value)==int(arg)):
        return "active"
    