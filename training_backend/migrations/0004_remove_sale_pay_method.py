# Generated by Django 3.2.9 on 2021-12-19 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_backend', '0003_sale_pay_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='pay_method',
        ),
    ]
