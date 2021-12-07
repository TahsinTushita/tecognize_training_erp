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
    user_profit = models.FloatField(blank=False)
    # photo = models.ImageField(blank=True)
    # user_cv = models.FileField()


class Retail_Customer(models.Model):
    cust_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    cust_name = models.CharField(max_length=100, blank=False)
    cust_phone = models.CharField(max_length=22, blank=False, unique=True)
    cust_email = models.CharField(max_length=255, blank=False)
    cust_address = models.CharField(max_length=200, blank=False)
    cust_organization = models.CharField(max_length=200, blank=False)
    cust_designation = models.CharField(max_length=150, blank=False)
    cust_total_fee = models.IntegerField(blank=True)
    cust_paid_fee = models.IntegerField(blank=True)
    cust_due_fee = models.IntegerField(blank=True)


class Corporate_Customer(models.Model):
    corp_id = models.CharField(
        max_length=100, blank=False, primary_key=True, unique=True
    )
    corp_name = models.CharField(max_length=100, blank=False)
    corp_phone = models.CharField(max_length=22, blank=False)
    corp_email = models.CharField(max_length=255, blank=False)
    corp_address = models.CharField(max_length=200, blank=False)
    corp_total_fee = models.IntegerField()
    corp_paid_fee = models.IntegerField()
    corp_due_fee = models.IntegerField()
    corp_units = models.IntegerField()


class Course(models.Model):
    course_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    course_name = models.CharField(max_length=100, blank=False, unique=True)
    regular_price = models.IntegerField()
    # outline = models.FileField()
    cat_id = models.ForeignKey(Category, db_column="cat_id", on_delete=models.CASCADE)


# class Batch(models.Model):
#     batch_id = models.CharField(max_length=30, blank=False)
#     regular_fee = models.IntegerField()
#     discount_fee = models.IntegerField()
#     ad_closed = models.BooleanField()
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


class Batch(models.Model):
    batch = models.CharField(max_length=30, blank=False)
    regular_fee = models.IntegerField()
    discount_fee = models.IntegerField()
    ad_closed = models.BooleanField()
    inst_id = models.ForeignKey(
        Instructor, db_column="inst_id", on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(User, db_column="user_id", on_delete=models.CASCADE)
    cust_id = models.ForeignKey(
        Retail_Customer,
        db_column="cust_id",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    corp_id = models.ForeignKey(
        Corporate_Customer,
        db_column="corp_id",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
