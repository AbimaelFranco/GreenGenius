# Generated by Django 4.1.1 on 2024-03-28 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alerta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerta',
            name='details',
        ),
    ]
