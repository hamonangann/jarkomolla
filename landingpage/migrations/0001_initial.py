# Generated by Django 4.0.4 on 2022-12-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Konten',
            fields=[
                ('idKonten', models.BigAutoField(primary_key=True, serialize=False)),
                ('judulKonten', models.CharField(max_length=30)),
                ('thumbnail', models.CharField(max_length=500)),
                ('isiKonten', models.TextField()),
            ],
        ),
    ]