# Generated by Django 4.2 on 2023-06-01 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='attributename',
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantapp.attributecategory'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
