# Generated by Django 4.0.4 on 2022-12-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=255)),
                ('no_telpon', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
    ]
