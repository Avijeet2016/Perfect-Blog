# Generated by Django 2.2 on 2020-05-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default/default.jpg', upload_to='profile_pics/'),
        ),
    ]
