from rest_framework import serializers
from training_backend.models import (
    Instructor,
    User,
    Retail_Customer,
    Corporate_Customer,
    Category,
    Course,
    Batch,
    Sale,
)


class NumberSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = (
            "inst_id",
            "inst_name",
            "inst_phone",
            "inst_email",
            "inst_address",
            "inst_organization",
            "inst_designation",
            "inst_profit",
            # "photo",
            # "inst_cv",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "user_id",
            "user_name",
            "user_phone",
            "user_email",
            "user_address",
            "user_designation",
            "user_profit",
            # "photo",
            # "inst_cv",
        )


class RetailCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail_Customer
        fields = (
            "cust_id",
            "cust_name",
            "cust_phone",
            "cust_email",
            "cust_address",
            "cust_organization",
            "cust_designation",
            "cust_total_fee",
            "cust_paid_fee",
            "cust_due_fee",
        )


class CorporateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate_Customer
        fields = (
            "corp_id",
            "corp_name",
            "corp_phone",
            "corp_email",
            "corp_address",
            "corp_total_fee",
            "corp_paid_fee",
            "corp_due_fee",
            "corp_units",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("cat_id", "cat_name")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("course_id", "course_name", "regular_price", "cat_id")


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = (
            "batch_id",
            "batch_fee",
            "admit_closed",
            "course_id",
            "inst_id",
        )


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = (
            "id",
            "regular_fee",
            "sale_fee",
            "paid_fee",
            "due_fee",
            "batch_id",
            "corp_id",
            "cust_id",
            "inst_id",
            "user_id",
        )
