# Generated by Django 4.0.4 on 2022-12-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url_gambar',
            field=models.TextField(default='https://www.pngkey.com/png/detail/233-2332677_image-500580-placeholder-transparent.png'),
        ),
    ]