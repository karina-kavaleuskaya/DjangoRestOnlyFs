# Generated by Django 5.0.3 on 2024-03-31 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_role_alter_role_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='cashback_points',
        ),
    ]
