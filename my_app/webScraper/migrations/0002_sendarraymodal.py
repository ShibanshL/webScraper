# Generated by Django 5.0.1 on 2024-01-07 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webScraper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sendArrayModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webScraper.webscrmodel')),
            ],
        ),
    ]
