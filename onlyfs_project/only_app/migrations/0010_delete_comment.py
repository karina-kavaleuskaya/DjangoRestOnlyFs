# Generated by Django 5.0.3 on 2024-04-14 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('only_app', '0009_remove_product_if_notif_sent_stock_if_notif_sent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
