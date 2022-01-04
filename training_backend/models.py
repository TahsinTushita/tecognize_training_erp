from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
import warnings

warnings.filterwarnings("ignore", "Field 'id' doesn't have a default value")

# Create your models here.


class Instructor(models.Model):
    inst_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    inst_name = models.CharField(max_length=100, blank=False)
    inst_phone = models.CharField(max_length=22, blank=False)
    inst_email = models.CharField(max_length=255, blank=False)
    inst_address = models.CharField(max_length=200, blank=False)
    inst_organization = models.CharField(max_length=200, blank=False)
    inst_designation = models.CharField(max_length=150, blank=False)
    inst_profit = models.FloatField(blank=False)
    inst_payable = models.IntegerField(blank=True)
    inst_paid = models.IntegerField(blank=True)
    inst_due = models.IntegerField(blank=True)
    # photo = models.ImageField(blank=True)
    # inst_cv = models.FileField()


class Category(models.Model):
    cat_id = models.CharField(max_length=10, blank=False, primary_key=True, unique=True)
    cat_name = models.CharField(max_length=100, blank=False)


class User(models.Model):
    user_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    user_name = models.CharField(max_length=100, blank=False)
    user_phone = models.CharField(max_length=22, blank=False)
    user_email = models.CharField(max_length=255, blank=False)
    user_address = models.CharField(max_length=200, blank=False)
    user_designation = models.CharField(max_length=150, blank=False)
    user_profit = models.FloatField()
    # photo = models.ImageField(blank=True)
    # user_cv = models.FileField()


class Customer(models.Model):
    cust_id = models.CharField(max_length=10, primary_key=True, unique=True, blank=True)
    cust_name = models.CharField(max_length=100, blank=True)
    cust_phone = models.CharField(max_length=22, unique=True, blank=True)
    cust_email = models.CharField(max_length=255, blank=True)
    cust_address = models.CharField(max_length=200, blank=True)
    cust_organization = models.CharField(max_length=200, blank=True, null=True)
    cust_designation = models.CharField(max_length=150, blank=True, null=True)
    cust_total_fee = models.IntegerField(blank=True)
    cust_paid_fee = models.IntegerField(blank=True)
    cust_due_fee = models.IntegerField(blank=True)
    cust_units = models.IntegerField()


# class Corporate_Customer(models.Model):
#     corp_id = models.CharField(
#         max_length=100, blank=False, primary_key=True, unique=True
#     )
#     corp_name = models.CharField(max_length=100, blank=False)
#     corp_phone = models.CharField(max_length=22, blank=False)
#     corp_email = models.CharField(max_length=255, blank=False)
#     corp_address = models.CharField(max_length=200, blank=False)
#     corp_total_fee = models.IntegerField()
#     corp_paid_fee = models.IntegerField()
#     corp_due_fee = models.IntegerField()
#     corp_units = models.IntegerField()


class Course(models.Model):
    course_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    course_name = models.CharField(max_length=100, blank=False, unique=True)
    regular_price = models.IntegerField()
    # outline = models.FileField()
    cat_id = models.ForeignKey(Category, db_column="cat_id", on_delete=models.CASCADE)


class Batch(models.Model):
    batch_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    batch_fee = models.IntegerField()
    inst_id = models.ForeignKey(
        Instructor, db_column="inst_id", on_delete=models.CASCADE
    )
    admit_closed = models.BooleanField()
    course_id = models.ForeignKey(
        Course, db_column="course_id", on_delete=models.CASCADE
    )
    inst_profit = models.FloatField(blank=False)


# class Sale(models.Model):
#     batch_id = models.ForeignKey(Batch, db_column="batch_id", on_delete=models.CASCADE)
#     regular_fee = models.IntegerField()
#     sale_fee = models.IntegerField()
#     installment1 = models.IntegerField()
#     installment2 = models.IntegerField()
#     installment3 = models.IntegerField()
#     installment4 = models.IntegerField()
#     due_fee = models.IntegerField()
#     inst_id = models.ForeignKey(
#         Instructor, db_column="inst_id", on_delete=models.CASCADE
#     )
#     user_id = models.ForeignKey(User, db_column="user_id", on_delete=models.CASCADE)
#     cust_id = models.ForeignKey(
#         Retail_Customer,
#         db_column="cust_id",
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#     )
#     corp_id = models.ForeignKey(
#         Corporate_Customer,
#         db_column="corp_id",
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#     )
#     pay_method = models.CharField(max_length=100)
#     check_ref_no = models.CharField(max_length=100)
#     curr_date = models.DateField()
#     check_date = models.DateField(blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True)
#     address = models.CharField(max_length=200, blank=True)
#     prev_receipts = models.CharField(max_length=100, blank=True)


class SaleReport(models.Model):
    cust_id = models.ForeignKey(Customer, db_column="cust_id", on_delete=models.CASCADE)
    batch_id = models.ForeignKey(Batch, db_column="batch_id", on_delete=models.CASCADE)
    regular_fee = models.IntegerField()
    batch_fee = models.IntegerField()
    installment1 = models.IntegerField()
    mr_no1 = models.IntegerField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    check_date1 = models.DateField(blank=True, null=True)
    check_ref_no1 = models.CharField(max_length=100, blank=True, null=True)
    pay_mode1 = models.CharField(max_length=100, blank=True, null=True)
    installment2 = models.IntegerField()
    mr_no2 = models.IntegerField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    check_date2 = models.DateField(blank=True, null=True)
    check_ref_no2 = models.CharField(max_length=100, blank=True, null=True)
    pay_mode2 = models.CharField(max_length=100, blank=True, null=True)
    installment3 = models.IntegerField()
    mr_no3 = models.IntegerField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    check_date3 = models.DateField(blank=True, null=True)
    check_ref_no3 = models.CharField(max_length=100, blank=True, null=True)
    pay_mode3 = models.CharField(max_length=100, blank=True, null=True)
    installment4 = models.IntegerField()
    mr_no4 = models.IntegerField(blank=True, null=True)
    date4 = models.DateField(blank=True, null=True)
    check_date4 = models.DateField(blank=True, null=True)
    check_ref_no4 = models.CharField(max_length=100, blank=True, null=True)
    pay_mode4 = models.CharField(max_length=100, blank=True, null=True)
    paid = models.IntegerField()
    due = models.IntegerField()
    inst_id = models.ForeignKey(
        Instructor, db_column="inst_id", on_delete=models.CASCADE
    )
    inst_profit = models.FloatField()
    user_id = models.ForeignKey(User, db_column="user_id", on_delete=models.CASCADE)
    user_profit = models.FloatField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
