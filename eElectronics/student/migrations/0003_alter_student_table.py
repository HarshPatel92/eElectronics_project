# Generated by Django 4.1.7 on 2023-03-02 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
    ]
