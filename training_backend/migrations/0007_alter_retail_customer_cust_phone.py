# Generated by Django 3.2.9 on 2021-12-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_backend', '0006_auto_20211207_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retail_customer',
            name='cust_phone',
            field=models.CharField(max_length=22, unique=True),
        ),
    ]