# Generated by Django 5.0.7 on 2024-07-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_menuitem_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='slug',
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]