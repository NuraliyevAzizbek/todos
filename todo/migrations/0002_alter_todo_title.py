# Generated by Django 4.2.16 on 2024-12-04 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
