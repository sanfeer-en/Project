# Generated by Django 4.2 on 2023-08-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0012_rename_production_rawmaterial_productionrawmaterial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='Varients',
            field=models.CharField(blank=True, choices=[('size', 'size'), ('addon', 'add-on'), ('extra', 'extra')], max_length=100, null=True),
        ),
    ]
