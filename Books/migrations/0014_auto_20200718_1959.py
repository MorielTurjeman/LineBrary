# Generated by Django 3.0.4 on 2020-07-18 16:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Books', '0013_auto_20200718_1428'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddBook',
            new_name='Contributions',
        ),
    ]
