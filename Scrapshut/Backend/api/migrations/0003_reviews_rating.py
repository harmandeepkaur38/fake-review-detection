# Generated by Django 3.0.3 on 2020-03-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.CharField(default=2, max_length=5),
            preserve_default=False,
        ),
    ]
