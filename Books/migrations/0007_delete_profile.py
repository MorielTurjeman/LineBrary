# Generated by Django 3.0.3 on 2020-07-14 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('Books', '0006_auto_20200713_1629'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
