# Generated by Django 5.0.3 on 2024-03-30 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(default='user', on_delete=django.db.models.deletion.PROTECT, to='users.role'),
        ),
    ]
