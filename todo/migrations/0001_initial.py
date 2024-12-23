# Generated by Django 4.2.16 on 2024-12-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_done', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'To-Do',
                'verbose_name_plural': 'To-Dos',
            },
        ),
    ]
