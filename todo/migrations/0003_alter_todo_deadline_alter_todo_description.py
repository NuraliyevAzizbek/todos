# Generated by Django 4.2.16 on 2024-12-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
