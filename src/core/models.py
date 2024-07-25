from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, null=True)
    comment = models.TextField()
    source_of_review = models.CharField(max_length=255)
    source_of_review_url = models.URLField(null=True)
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ["-date_published"]
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        db_table = "menus"
