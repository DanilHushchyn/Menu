# Generated by Django 5.0.7 on 2024-07-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_menuitem_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(default=None, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
