# Generated by Django 3.2.8 on 2021-10-23 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_auto_20211023_0806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='taskName',
            new_name='task_name',
        ),
    ]