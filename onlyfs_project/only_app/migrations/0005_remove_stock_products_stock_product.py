# Generated by Django 5.0.3 on 2024-04-13 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('only_app', '0004_remove_stock_product_stock_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='products',
        ),
        migrations.AddField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='only_app.product'),
        ),
    ]