# Generated by Django 5.0.3 on 2024-03-30 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.PROTECT, to='users.role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('user', 'User'), ('creator', 'Creator'), ('superuser', 'Superuser')], default='user', max_length=20),
        ),
    ]