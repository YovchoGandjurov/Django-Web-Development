# Generated by Django 2.2.1 on 2019-05-10 09:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileUser',
            new_name='Profile',
        ),
    ]
