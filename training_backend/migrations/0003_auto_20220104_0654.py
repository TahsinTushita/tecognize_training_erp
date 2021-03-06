# Generated by Django 3.2.9 on 2022-01-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_backend', '0002_auto_20211226_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='inst_due',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructor',
            name='inst_paid',
            field=models.IntegerField(blank=True, default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructor',
            name='inst_payable',
            field=models.IntegerField(blank=True, default=11000),
            preserve_default=False,
        ),
    ]
