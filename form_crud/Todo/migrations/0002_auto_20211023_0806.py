# Generated by Django 3.2.8 on 2021-10-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='gender',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]