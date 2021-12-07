from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
import warnings

warnings.filterwarnings("ignore", "Field 'id' doesn't have a default value")

# Create your models here.


class Instructor(models.Model):
    inst_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=22, blank=False)
    email = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=200, blank=False)
    organization = models.CharField(max_length=200, blank=False)
    designation = models.CharField(max_length=150, blank=False)
    profit = models.FloatField(blank=False)
    # photo = models.ImageField(blank=True)
    # inst_cv = models.FileField()


class Category(models.Model):
    cat_id = models.CharField(max_length=10, blank=False, primary_key=True, unique=True)
    cat_name = models.CharField(max_length=100, blank=False)


class User(models.Model):
    user_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=22, blank=False)
    email = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=200, blank=False)
    designation = models.CharField(max_length=150, blank=False)
    profit = models.FloatField(blank=False)
    # photo = models.ImageField(blank=True)
    # user_cv = models.FileField()


class Retail_Customer(models.Model):
    cust_id = models.CharField(
        max_length=10, blank=False, primary_key=True, unique=True
    )
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=22, blank=False)
    email = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=200, blank=False)
    organization = models.CharField(max_length=200, blank=False)
    designation = models.CharField(max_length=150, blank=False)
    total_fee = models.IntegerField()
    paid_fee = models.IntegerField()
    due_fee = models.IntegerField()


class Corporate_Customer(models.Model):
    corp_id = models.CharField(
        max_length=100, blank=False, primary_key=True, unique=True
    )
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=22, blank=False)
    email = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=200, blank=False)
    total_fee = models.IntegerField()
    paid_fee = models.IntegerField()
    due_fee = models.IntegerField()
    units = models.IntegerField()


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
