# Generated by Django 4.2 on 2023-06-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0004_product_category_fr_product_is_for_sale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Is_for_sale',
            field=models.BooleanField(default=False),
        ),
    ]
