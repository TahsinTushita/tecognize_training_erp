# Generated by Django 3.2.9 on 2021-12-07 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_backend', '0010_auto_20211207_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='batch',
            new_name='batch_id',
        ),
    ]
