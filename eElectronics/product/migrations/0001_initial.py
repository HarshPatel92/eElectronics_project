# Generated by Django 4.1.7 on 2023-03-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=100)),
                ('pPrice', models.FloatField()),
                ('pQty', models.IntegerField()),
                ('pDesc', models.CharField(max_length=100, null=True)),
                ('pStatus', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
