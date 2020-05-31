# Generated by Django 2.2 on 2020-05-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200531_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, default='default/default.jpg', null=True, upload_to='about_pics/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default/default.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]