from django import template

register = template.Library()


@register.filter
def stripleadingzero(string):
    return string.lstrip('0')
@register.filter
def query_is_nono(obj):
    return True if len(list(obj))!=0 else False
@register.filter
def j_info(string):
    if string=='none':
        return False
    else:
        return  True