# Generated by Django 3.2.9 on 2021-12-06 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_backend', '0010_remove_course_outline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corporate_customer',
            name='organization',
        ),
    ]
