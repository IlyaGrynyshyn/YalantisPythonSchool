# Generated by Django 3.0.8 on 2021-05-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210503_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='small_description',
            field=models.TextField(verbose_name='Коротний опис'),
        ),
    ]
