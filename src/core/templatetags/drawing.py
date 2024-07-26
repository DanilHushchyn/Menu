from django import template

register = template.Library()


@register.inclusion_tag('core/menu.html')
def draw_menu(menu):
    return {
        "menu": menu,
    }
