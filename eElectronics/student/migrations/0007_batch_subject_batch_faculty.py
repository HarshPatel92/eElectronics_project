# Generated by Django 4.1.7 on 2023-03-02 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_batch_faculty_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='Subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.subject'),
        ),
        migrations.AddField(
            model_name='batch',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.faculty'),
        ),
    ]
