# Generated by Django 4.2.6 on 2023-11-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0002_delete_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisherhouse',
            name='year_established',
            field=models.IntegerField(null=True),
        ),
    ]
