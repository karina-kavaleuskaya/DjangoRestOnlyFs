# Generated by Django 5.0.3 on 2024-03-31 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('only_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_blurred',
            field=models.BooleanField(default=True),
        ),
    ]
