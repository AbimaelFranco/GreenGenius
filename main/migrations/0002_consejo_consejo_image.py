# Generated by Django 4.1.1 on 2024-04-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consejo',
            name='consejo_image',
            field=models.ImageField(default='main_consejos/default.png', upload_to='main_consejos'),
        ),
    ]
