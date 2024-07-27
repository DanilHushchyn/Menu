from django import template
from django.db.models import QuerySet

from src.core.models import MenuItem, Menu

register = template.Library()


def get_tree_recursively(root_item: MenuItem,
                         items: QuerySet[MenuItem]) -> dict:
    """
    Method for recursively traversing root menu
    elements to form a tree structure
    :param root_item: root menu item
    :param items: all menu items
    :return: tree structure
    """
    childs = []
    for item in items:
        if item.parent_id == root_item.id:
            childs.append(
                get_tree_recursively(item, items)
            )
    result = {
        "page_id": root_item.page_id,
        "page_name": root_item.page.name,
        "childs": childs,
    }

    return result


@register.inclusion_tag('core/menu.html')
def draw_menu(menu: Menu):
    """
    General method for rendering menu
    :param menu: menu for rendering
    """
    menu_item_list = []

    items = menu.items.all()
    root_items = []
    # Get root items of menu
    for item in items:
        if item.parent is None:
            root_items.append(item)

    # Get all root items trees recursively
    for item in root_items:
        menu_item = get_tree_recursively(item, items)
        menu_item_list.append(menu_item)

    return {
        "menu": menu,
        "menu_item_list": menu_item_list,
    }
