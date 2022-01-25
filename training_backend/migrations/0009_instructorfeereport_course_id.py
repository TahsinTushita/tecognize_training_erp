# Generated by Django 3.2.9 on 2022-01-25 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training_backend', '0008_alter_batch_batch_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructorfeereport',
            name='course_id',
            field=models.ForeignKey(db_column='course_id', default='AWS0002', on_delete=django.db.models.deletion.CASCADE, to='training_backend.course'),
            preserve_default=False,
        ),
    ]
