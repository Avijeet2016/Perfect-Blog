# Generated by Django 2.2 on 2020-05-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='about_pics/'),
        ),
    ]
