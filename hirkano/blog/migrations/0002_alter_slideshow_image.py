# Generated by Django 4.1.3 on 2022-12-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='image',
            field=models.ImageField(upload_to='slide_show/images.'),
        ),
    ]