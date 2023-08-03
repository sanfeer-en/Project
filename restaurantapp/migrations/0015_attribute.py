# Generated by Django 4.2 on 2023-08-03 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0014_delete_attribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Varients', models.CharField(blank=True, choices=[('size', 'size'), ('addon', 'add-on'), ('extra', 'extra')], max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('attribute_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.attributecategory')),
            ],
        ),
    ]
