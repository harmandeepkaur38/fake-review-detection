# Generated by Django 3.0.3 on 2020-03-03 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('review', models.CharField(max_length=100000000000000)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]