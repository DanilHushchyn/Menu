from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date_published"]
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        db_table = "menus"


class Page(models.Model):
    name = models.CharField(max_length=255, unique=True)
    menus = models.ManyToManyField(Menu)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        db_table = "pages"


class MenuItem(models.Model):
    page = models.ForeignKey(Page,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, related_name='childs',
                               blank=True,
                               on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name='items',
                             on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def count_nested(self, obj, level):
        if obj.parent is not None:
            level = level + 1
            return self.count_nested(obj.parent, level)
        return level

    def __str__(self):
        if self.parent is None:
            level_nested = 0
        else:
            level_nested = self.count_nested(self, 0)

        self.childs.all()
        return (f"Page - {self.page.name}; "
                f"Menu - {self.menu.name};"
                f"LevelNested - {level_nested}")

    class Meta:
        ordering = ["order"]
        verbose_name = "MenuItem"
        verbose_name_plural = "MenuItems"
        db_table = "menu_items"
