# Generated by Django 4.0.4 on 2022-12-10 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_url_gambar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id']},
        ),
    ]
