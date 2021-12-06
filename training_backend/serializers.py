from rest_framework import serializers
from training_backend.models import (
    Instructor,
    User,
    Retail_Customer,
    Corporate_Customer,
    Category,
    Course,
    Batch,
)


class NumberSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = (
            "inst_id",
            "name",
            "phone",
            "email",
            "address",
            "organization",
            "designation",
            "profit",
            # "photo",
            # "inst_cv",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "user_id",
            "name",
            "phone",
            "email",
            "address",
            "designation",
            "profit",
            # "photo",
            # "inst_cv",
        )


class RetailCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail_Customer
        fields = (
            "cust_id",
            "name",
            "phone",
            "email",
            "address",
            "organization",
            "designation",
            "total_fee",
            "paid_fee",
            "due_fee",
        )


class CorporateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate_Customer
        fields = (
            "corp_id",
            "name",
            "phone",
            "email",
            "address",
            "organization",
            "total_fee",
            "paid_fee",
            "due_fee",
            "units",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("cat_id", "name")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("course_id", "name", "regular_price", "outline", "cat_id")


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = (
            "batch_id",
            "regular_fee",
            "discount_fee",
            "ad_closed",
            "corp_id",
            "cust_id",
            "inst_id",
            "user_id",
        )
