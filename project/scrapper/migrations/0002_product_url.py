# Generated by Django 4.0.6 on 2023-02-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
