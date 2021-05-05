# Generated by Django 3.0.8 on 2021-04-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва курсу')),
                ('slug', models.SlugField(unique=True)),
                ('start_date', models.DateField(verbose_name='Дата початку')),
                ('end_date', models.DateField(verbose_name='Дата закінчення')),
                ('quantity_lections', models.IntegerField(verbose_name='Кількість лекцій')),
                ('photo', models.ImageField(upload_to='', verbose_name='Зображення')),
                ('description', models.TextField(null=True, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
            },
        ),
    ]
