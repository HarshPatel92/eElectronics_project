# Generated by Django 4.1.7 on 2023-03-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0002_addfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
