# Generated by Django 5.0.3 on 2024-04-13 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('only_app', '0005_remove_stock_products_stock_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
    ]