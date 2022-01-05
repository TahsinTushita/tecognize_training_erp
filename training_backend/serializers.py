from rest_framework import serializers
from training_backend.models import (
    Instructor,
    User,
    Customer,
    # Corporate_Customer,
    Category,
    Course,
    Batch,
    # Sale,
    SaleReport,
    InstructorFeeReport,
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
            "inst_payable",
            "inst_paid",
            "inst_due"
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


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
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
            "cust_units",
        )


# class CorporateCustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Corporate_Customer
#         fields = (
#             "corp_id",
#             "corp_name",
#             "corp_phone",
#             "corp_email",
#             "corp_address",
#             "corp_total_fee",
#             "corp_paid_fee",
#             "corp_due_fee",
#             "corp_units",
#         )


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
            "inst_profit",
        )

    # class SaleSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Sale
    #     fields = (
    #         "id",
    #         "batch_id",
    #         "regular_fee",
    #         "sale_fee",
    #         "installment1",
    #         "installment2",
    #         "installment3",
    #         "installment4",
    #         "due_fee",
    #         "inst_id",
    #         "user_id",
    #         "cust_id",
    #         "corp_id",
    #         "pay_method",
    #         "check_ref_no",
    #         "curr_date",
    #         "check_date",
    #         "name",
    #         "address",
    #         "prev_receipts",
    #     )


class SaleReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleReport
        fields = (
            "cust_id",
            "batch_id",
            "regular_fee",
            "batch_fee",
            "installment1",
            "mr_no1",
            "date1",
            "check_date1",
            "check_ref_no1",
            "pay_mode1",
            "installment2",
            "mr_no2",
            "date2",
            "check_date2",
            "check_ref_no2",
            "pay_mode2",
            "installment3",
            "mr_no3",
            "date3",
            "check_date3",
            "check_ref_no3",
            "pay_mode3",
            "installment4",
            "mr_no4",
            "date4",
            "check_date4",
            "check_ref_no4",
            "pay_mode4",
            "paid",
            "due",
            "inst_id",
            "inst_profit",
            "user_id",
            "user_profit",
            "remarks",
        )


class InstructorFeeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorFeeReport
        fields = (
            "id",
            "inst_id",
            "batch_id",
            "total_sale",
            "pay_received",
            "total_payable",
            "paid",
            "due",
            "date",
            "pay_mode",
            "check_date",
            "check_no",
        )
