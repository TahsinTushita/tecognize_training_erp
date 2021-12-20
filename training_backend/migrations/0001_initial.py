# Generated by Django 3.2.9 on 2021-12-20 11:12

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
            name='Corporate_Customer',
            fields=[
                ('corp_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('corp_name', models.CharField(max_length=100)),
                ('corp_phone', models.CharField(max_length=22)),
                ('corp_email', models.CharField(max_length=255)),
                ('corp_address', models.CharField(max_length=200)),
                ('corp_total_fee', models.IntegerField()),
                ('corp_paid_fee', models.IntegerField()),
                ('corp_due_fee', models.IntegerField()),
                ('corp_units', models.IntegerField()),
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
            name='Retail_Customer',
            fields=[
                ('cust_id', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('cust_name', models.CharField(blank=True, max_length=100)),
                ('cust_phone', models.CharField(blank=True, max_length=22, unique=True)),
                ('cust_email', models.CharField(blank=True, max_length=255)),
                ('cust_address', models.CharField(blank=True, max_length=200)),
                ('cust_organization', models.CharField(blank=True, max_length=200)),
                ('cust_designation', models.CharField(blank=True, max_length=150)),
                ('cust_total_fee', models.IntegerField(blank=True)),
                ('cust_paid_fee', models.IntegerField(blank=True)),
                ('cust_due_fee', models.IntegerField(blank=True)),
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
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_fee', models.IntegerField()),
                ('sale_fee', models.IntegerField()),
                ('installment1', models.IntegerField()),
                ('installment2', models.IntegerField()),
                ('installment3', models.IntegerField()),
                ('installment4', models.IntegerField()),
                ('due_fee', models.IntegerField()),
                ('pay_method', models.CharField(max_length=100)),
                ('check_ref_no', models.CharField(max_length=100)),
                ('curr_date', models.DateField()),
                ('check_date', models.DateField(blank=True, null=True)),
                ('batch_id', models.ForeignKey(db_column='batch_id', on_delete=django.db.models.deletion.CASCADE, to='training_backend.batch')),
                ('corp_id', models.ForeignKey(blank=True, db_column='corp_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='training_backend.corporate_customer')),
                ('cust_id', models.ForeignKey(blank=True, db_column='cust_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='training_backend.retail_customer')),
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