# Generated by Django 3.2.9 on 2022-01-05 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("training_backend", "0003_auto_20220104_0654"),
    ]

    operations = [
        migrations.CreateModel(
            name="InstructorFeeReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, verbose_name="ID"
                    ),
                ),
                ("total_sale", models.IntegerField()),
                ("pay_received", models.IntegerField()),
                ("total_payable", models.IntegerField()),
                ("paid", models.IntegerField()),
                ("due", models.IntegerField()),
                ("date", models.DateField(blank=True, null=True)),
                ("pay_mode", models.CharField(blank=True, max_length=100, null=True)),
                ("check_date", models.DateField(blank=True, null=True)),
                (
                    "batch_id",
                    models.ForeignKey(
                        db_column="batch_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="training_backend.batch",
                    ),
                ),
                (
                    "inst_id",
                    models.ForeignKey(
                        db_column="inst_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="training_backend.instructor",
                    ),
                ),
            ],
        ),
    ]
