# Generated by Django 5.0.3 on 2024-04-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('only_app', '0002_productimage_is_blurred'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='if_notif_sent',
            field=models.BooleanField(default=False),
        ),
    ]