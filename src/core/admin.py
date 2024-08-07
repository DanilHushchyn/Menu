from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django import forms

from src.core.models import Menu, Page, MenuItem


@admin.register(Menu)
class MenuAdminClass(ModelAdmin):
    """
    Admin configuration for model Menu.
    """
    pass


@admin.register(Page)
class PageAdminClass(ModelAdmin):
    """
    Admin configuration for model Page.
    """
    pass


class MenuItemForm(forms.ModelForm):
    """
    ModelForm configuration for model MenuItem.
    for admin panel class MenuItemAdminClass
    """
    class Meta:
        model = MenuItem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
            In this method, I exclude the possibility of the 
            Current element choosing itself as a Parent element
        """
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            pq = (self.fields["parent"].queryset
                  .exclude(id=instance.pk))
            self.fields["parent"].queryset = pq

    def save(self, commit=True):
        """
            If a menu item has a parent, it will be part of its parent's menu,
            regardless of what was selected in the admin panel.
            This is the best option in my opinion.
        """
        instance = super().save(commit=False)
        parent = instance.parent
        if parent:
            instance.menu_id = parent.menu.id
        return instance


@admin.register(MenuItem)
class MenuItemAdminClass(ModelAdmin):
    """
    Admin configuration for model MenuItem.
    """
    list_filter = ["menu", ]
    form = MenuItemForm
