# Generated by Django 3.2.9 on 2021-12-26 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('batch_fee', models.IntegerField()),
                ('admit_closed', models.BooleanField()),
                ('inst_profit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('cat_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('cust_name', models.CharField(blank=True, max_length=100)),
                ('cust_phone', models.CharField(blank=True, max_length=22, unique=True)),
                ('cust_email', models.CharField(blank=True, max_length=255)),
                ('cust_address', models.CharField(blank=True, max_length=200)),
                ('cust_organization', models.CharField(blank=True, max_length=200, null=True)),
                ('cust_designation', models.CharField(blank=True, max_length=150, null=True)),
                ('cust_total_fee', models.IntegerField(blank=True)),
                ('cust_paid_fee', models.IntegerField(blank=True)),
                ('cust_due_fee', models.IntegerField(blank=True)),
                ('cust_units', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('inst_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('inst_name', models.CharField(max_length=100)),
                ('inst_phone', models.CharField(max_length=22)),
                ('inst_email', models.CharField(max_length=255)),
                ('inst_address', models.CharField(max_length=200)),
                ('inst_organization', models.CharField(max_length=200)),
                ('inst_designation', models.CharField(max_length=150)),
                ('inst_profit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=22)),
                ('user_email', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=200)),
                ('user_designation', models.CharField(max_length=150)),
                ('user_profit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SaleReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_fee', models.IntegerField()),
                ('batch_fee', models.IntegerField()),
                ('installment1', models.IntegerField()),
                ('mr_no1', models.IntegerField(blank=True, null=True)),
                ('date1', models.DateField(blank=True, null=True)),
                ('check_date1', models.DateField(blank=True, null=True)),
                ('check_ref_no1', models.CharField(max_length=100)),
                ('pay_mode1', models.CharField(blank=True, max_length=100, null=True)),
                ('installment2', models.IntegerField()),
                ('mr_no2', models.IntegerField(blank=True, null=True)),
                ('date2', models.DateField(blank=True, null=True)),
                ('check_date2', models.DateField(blank=True, null=True)),
                ('check_ref_no2', models.CharField(max_length=100)),
                ('pay_mode2', models.CharField(blank=True, max_length=100, null=True)),
                ('installment3', models.IntegerField()),
                ('mr_no3', models.IntegerField(blank=True, null=True)),
                ('date3', models.DateField(blank=True, null=True)),
                ('check_date3', models.DateField(blank=True, null=True)),
                ('check_ref_no3', models.CharField(max_length=100)),
                ('pay_mode3', models.CharField(blank=True, max_length=100, null=True)),
                ('installment4', models.IntegerField()),
                ('mr_no4', models.IntegerField(blank=True, null=True)),
                ('date4', models.DateField(blank=True, null=True)),
                ('check_date4', models.DateField(blank=True, null=True)),
                ('check_ref_no4', models.CharField(max_length=100)),
                ('pay_mode4', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.IntegerField()),
                ('due', models.IntegerField()),
                ('inst_profit', models.FloatField()),
                ('user_profit', models.FloatField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('batch_id', models.ForeignKey(db_column='batch_id', on_delete=django.db.models.deletion.CASCADE, to='training_backend.batch')),
                ('cust_id', models.ForeignKey(db_column='cust_id', on_delete=django.db.models.deletion.CASCADE, to='training_backend.customer')),
                ('inst_id', models.ForeignKey(db_column='inst_id', on_delete=django.db.models.deletion.CASCADE, to='training_backend.instructor')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='training_backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=100, unique=True)),
                ('regular_price', models.IntegerField()),
                ('cat_id', models.ForeignKey(db_column='cat_id', on_delete=django.db.models.deletion.CASCADE, to='training_backend.category')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course_id',
            field=models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='training_backend.course'),
        ),
        migrations.AddField(
            model_name='batch',
            name='inst_id',
            field=models.ForeignKey(db_column='inst_id', on_delete=django.db.models.deletion.CASCADE, to='training_backend.instructor'),
        ),
    ]
