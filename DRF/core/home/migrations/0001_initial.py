# Generated by Django 4.0 on 2021-12-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.ImageField(default=18, upload_to='')),
                ('father_name', models.CharField(max_length=100)),
            ],
        ),
    ]