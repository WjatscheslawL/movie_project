# Generated by Django 5.0.7 on 2024-07-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название Filma')),
                ('autor', models.CharField(max_length=50, verbose_name='Пользователь')),
                ('short_description', models.CharField(max_length=200, verbose_name='Краткое описание Filma')),
                ('text', models.TextField(verbose_name='OT3bIB')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
            },
        ),
    ]
