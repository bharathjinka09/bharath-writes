# Generated by Django 2.2 on 2020-05-14 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_delete_postuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='owner',
        ),
    ]