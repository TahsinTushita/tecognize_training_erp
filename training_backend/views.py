from django.db.models import query
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, serializers
from rest_framework.relations import ManyRelatedField

from django.core.serializers import serialize
import json
from django.db import connection

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
)
from training_backend.serializers import (
    InstructorSerializer,
    UserSerializer,
    CustomerSerializer,
    # CorporateCustomerSerializer,
    CategorySerializer,
    CourseSerializer,
    BatchSerializer,
    # SaleSerializer,
    SaleReportSerializer,
    # NumberSerializer,
)
from rest_framework.decorators import api_view

# Create your views here.


# Instructor


@api_view(["GET", "POST"])
def instructor_list(request):
    if request.method == "GET":
        instructors = Instructor.objects.all()

        inst_name = request.GET.get("inst_name", None)
        if inst_name is not None:
            instructors = instructors.filter(inst_name__icontains=inst_name)

        instructors_serializer = InstructorSerializer(instructors, many=True)
        return JsonResponse(instructors_serializer.data, safe=False)

    elif request.method == "POST":
        instructor_data = JSONParser().parse(request)
        instructors_serializer = InstructorSerializer(data=instructor_data)
        if instructors_serializer.is_valid():
            instructors_serializer.save()
            return JsonResponse(
                instructors_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            instructors_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def instructor_detail(request, pk):
    try:
        instructor = Instructor.objects.get(pk=pk)
    except Instructor.DoesNotExist:
        return JsonResponse(
            {"message": "The instructor does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        instructor_serializer = InstructorSerializer(instructor)
        return JsonResponse(instructor_serializer.data)

    elif request.method == "PUT":
        instructor_data = JSONParser().parse(request)
        instructors_serializer = InstructorSerializer(data=instructor_data)
        if instructors_serializer.is_valid():
            instructors_serializer.save()
            return JsonResponse(instructors_serializer.data)
        return JsonResponse(
            instructors_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

        # cursor = connection.cursor()
        # query = "SELECT COUNT(inst_id) AS NumberOfInstructors FROM training_backend_instructor"

        # cursor.execute(query)
        # r = cursor.fetchone()
        # print(r)
        # return JsonResponse(r, safe=False)

    elif request.method == "DELETE":
        instructor.delete()
        return JsonResponse(
            {"message": "Instructor was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def instructor_count(request):
    if request.method == "GET":
        # print(number_of_instructors)
        # instructors_serializer = NumberSerializer(number_of_instructors)
        # instructors_serializer = serializers.serialize("json", number_of_instructors)
        # data = serializers.serialize("json", list(number_of_instructors))
        # print(data)

        # return JsonResponse(data, safe=False)
        # permission_serialize = json.loads(serialize("json", number_of_instructors))
        # return JsonResponse({"data": permission_serialize})
        cursor = connection.cursor()
        query = "SELECT COUNT(inst_id) AS NumberOfInstructors FROM training_backend_instructor"

        cursor.execute(query)
        r = cursor.fetchone()
        print(r)
        return JsonResponse(r, safe=False)


# objectQuerySet = ConventionCard.objects.filter(ownerUser = user)
# data = serializers.serialize('json', list(objectQuerySet), fields=('fileName','id'))

# User


@api_view(["GET", "POST"])
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()

        user_name = request.GET.get("user_name", None)
        if user_name is not None:
            users = users.filter(user_name__icontains=user_name)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse(
            {"message": "The user does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return JsonResponse(
            {"message": "User was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def user_count(request):
    if request.method == "GET":
        cursor = connection.cursor()
        query = "SELECT COUNT(user_id) AS NumberOfUsers FROM training_backend_user"

        cursor.execute(query)
        r = cursor.fetchone()
        print(r)
        return JsonResponse(r, safe=False)


# Category


@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()

        cat_name = request.GET.get("cat_name", None)
        if cat_name is not None:
            categories = categories.filter(cat_name__icontains=cat_name)

        categories_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)

    elif request.method == "POST":
        category_data = JSONParser().parse(request)
        categories_serializer = CategorySerializer(data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse(
                categories_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JsonResponse(
            {"message": "The category does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        category_serializer = CategorySerializer(category)
        return JsonResponse(category_serializer.data)

    elif request.method == "PUT":
        category_data = JSONParser().parse(request)
        categories_serializer = CategorySerializer(data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse(categories_serializer.data)
        return JsonResponse(
            categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        category.delete()
        return JsonResponse(
            {"message": "Category was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def category_count(request):
    if request.method == "GET":
        cursor = connection.cursor()
        query = (
            "SELECT COUNT(cat_id) AS NumberOfcategories FROM training_backend_category"
        )

        cursor.execute(query)
        r = cursor.fetchone()
        print(r)
        return JsonResponse(r, safe=False)


# Course


@api_view(["GET", "POST"])
def course_list(request):
    if request.method == "GET":
        cursor = connection.cursor()
        query = "SELECT training_backend_course.course_id,training_backend_course.course_name, training_backend_course.regular_price,training_backend_category.cat_name FROM training_backend_course INNER JOIN training_backend_category ON training_backend_course.cat_id=training_backend_category.cat_id"

        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return JsonResponse(
            [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
        )

    elif request.method == "POST":
        course_data = JSONParser().parse(request)
        courses_serializer = CourseSerializer(data=course_data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return JsonResponse(courses_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            courses_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return JsonResponse(
            {"message": "The course does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        course_serializer = CourseSerializer(course)
        return JsonResponse(course_serializer.data)

    elif request.method == "PUT":
        course_data = JSONParser().parse(request)
        courses_serializer = CourseSerializer(data=course_data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return JsonResponse(courses_serializer.data)
        return JsonResponse(
            courses_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        course.delete()
        return JsonResponse(
            {"message": "Course was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def course_count(request):
    if request.method == "GET":
        cursor = connection.cursor()
        query = (
            "SELECT COUNT(course_id) AS NumberOfcourses FROM training_backend_course"
        )

        cursor.execute(query)
        r = cursor.fetchone()
        print(r)
        return JsonResponse(r, safe=False)


# Batch


@api_view(["GET", "POST"])
def batch_list(request):
    if request.method == "GET":
        batches = Batch.objects.all()

        # course_id = request.GET.get("course_id", None)
        # if course_id is not None:
        #     batches = batches.filter(course_id__icontains=course_id)

        batches_serializer = BatchSerializer(batches, many=True)
        return JsonResponse(batches_serializer.data, safe=False)

    elif request.method == "POST":
        batch_data = JSONParser().parse(request)
        batches_serializer = BatchSerializer(data=batch_data)
        if batches_serializer.is_valid():
            batches_serializer.save()
            return JsonResponse(batches_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            batches_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def batch_detail(request, pk):
    try:
        batch = Batch.objects.get(pk=pk)
    except Batch.DoesNotExist:
        return JsonResponse(
            {"message": "The batch does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        batch_serializer = BatchSerializer(batch)
        return JsonResponse(batch_serializer.data)

    elif request.method == "PUT":
        batch_data = JSONParser().parse(request)
        batches_serializer = BatchSerializer(data=batch_data)
        if batches_serializer.is_valid():
            batches_serializer.save()
            return JsonResponse(batches_serializer.data)
        return JsonResponse(
            batches_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        batch.delete()
        return JsonResponse(
            {"message": "Batch was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def batch_count(request):
    if request.method == "GET":
        cursor = connection.cursor()
        query = "SELECT COUNT(batch_id) AS NumberOfbatches FROM training_backend_batch"

        cursor.execute(query)
        r = cursor.fetchone()
        print(r)
        return JsonResponse(r, safe=False)


@api_view(["GET"])
def batch_by_course(request):
    # batches = Batch.objects.all()
    course_id = request.GET.get("course_id", None)
    cursor = connection.cursor()
    query = "SELECT batch_id from training_backend_batch WHERE course_id=%s"

    cursor.execute(query, params=course_id)
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def batch_ids(request):
    cursor = connection.cursor()
    query = "SELECT batch_id,course_id FROM training_backend_batch"

    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def batch_list_table(request):
    cursor = connection.cursor()
    query = "SELECT training_backend_batch.batch_id,training_backend_batch.batch_fee,training_backend_batch.admit_closed,training_backend_course.course_name,training_backend_instructor.inst_name FROM training_backend_batch INNER JOIN training_backend_course ON training_backend_batch.course_id=training_backend_course.course_id INNER JOIN training_backend_instructor ON training_backend_batch.inst_id=training_backend_instructor.inst_id"

    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["PUT"])
def batch_admission(request, pk):
    cursor = connection.cursor()
    query = "UPDATE training_backend_batch SET admit_closed=(NOT admit_closed) WHERE batch_id=%s"

    cursor.execute(query, params=(pk))
    r = cursor.fetchone()
    return JsonResponse(r, safe=False)


# Retail Customer


@api_view(["GET", "POST"])
def customer_list(request):
    if request.method == "GET":
        customers = Customer.objects.all()

        cust_phone = request.GET.get("cust_phone", None)
        if cust_phone is not None:
            customers = customers.filter(cust_phone__icontains=cust_phone)

        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)

    elif request.method == "POST":
        customer_data = JSONParser().parse(request)
        customers_serializer = CustomerSerializer(data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse(
                customers_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return JsonResponse(
            {"message": "The customer does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data)

    elif request.method == "PUT":
        customer_data = JSONParser().parse(request)
        customers_serializer = CustomerSerializer(data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse(customers_serializer.data)
        return JsonResponse(
            customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        customer.delete()
        return JsonResponse(
            {"message": "customer was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def customer_count(request):
    if request.method == "GET":
        cursor = connection.cursor()
        query = "SELECT COUNT(cust_id) AS NumberOfRetailCustomers FROM training_backend_customer"

        cursor.execute(query)
        r = cursor.fetchone()
        print(r)
        return JsonResponse(r, safe=False)


@api_view(["PUT"])
def customer_fee_update(request):
    cursor = connection.cursor()
    customer_data = JSONParser().parse(request)
    # customer_data = json.load(request)
    print(customer_data)
    query = "UPDATE training_backend_customer SET cust_total_fee=%s,cust_paid_fee=%s,cust_due_fee=%s,cust_units=%s WHERE cust_id=%s"

    cursor.execute(
        query,
        params=(
            customer_data["cust_total_fee"],
            customer_data["cust_paid_fee"],
            customer_data["cust_due_fee"],
            customer_data["cust_units"],
            customer_data["cust_id"],
        ),
    )
    r = cursor.fetchone()
    return JsonResponse(r, safe=False)


# @api_view(["GET"])
# def retail_due_batches(request):
#     cursor = connection.cursor()
#     customer_data = JSONParser().parse(request)
#     query = ""


# Corporate customer


# @api_view(["GET", "POST"])
# def corporate_customer_list(request):
#     if request.method == "GET":
#         corporate_customers = Corporate_Customer.objects.all()

#         corp_name = request.GET.get("corp_name", None)
#         if corp_name is not None:
#             corporate_customers = corporate_customers.filter(
#                 corp_name__icontains=corp_name
#             )

#         corporate_customers_serializer = CorporateCustomerSerializer(
#             corporate_customers, many=True
#         )
#         return JsonResponse(corporate_customers_serializer.data, safe=False)

#     elif request.method == "POST":
#         corporate_customer_data = JSONParser().parse(request)
#         corporate_customers_serializer = CorporateCustomerSerializer(
#             data=corporate_customer_data
#         )
#         if corporate_customers_serializer.is_valid():
#             corporate_customers_serializer.save()
#             return JsonResponse(
#                 corporate_customers_serializer.data, status=status.HTTP_201_CREATED
#             )
#         return JsonResponse(
#             corporate_customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )


# @api_view(["GET", "PUT", "DELETE"])
# def corporate_customer_detail(request, pk):
#     try:
#         corporate_customer = Corporate_Customer.objects.get(pk=pk)
#     except Corporate_Customer.DoesNotExist:
#         return JsonResponse(
#             {"message": "The corporate_customer does not exist"},
#             status=status.HTTP_404_NOT_FOUND,
#         )

#     if request.method == "GET":
#         corporate_customer_serializer = CorporateCustomerSerializer(corporate_customer)
#         return JsonResponse(corporate_customer_serializer.data)

#     elif request.method == "PUT":
#         corporate_customer_data = JSONParser().parse(request)
#         corporate_customers_serializer = CorporateCustomerSerializer(
#             data=corporate_customer_data
#         )
#         if corporate_customers_serializer.is_valid():
#             corporate_customers_serializer.save()
#             return JsonResponse(corporate_customers_serializer.data)
#         return JsonResponse(
#             corporate_customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )

#     elif request.method == "DELETE":
#         corporate_customer.delete()
#         return JsonResponse(
#             {"message": "corporate_customer was deleted successfully!"},
#             status=status.HTTP_204_NO_CONTENT,
#         )


# @api_view(["GET"])
# def corporate_customer_count(request):
#     if request.method == "GET":
#         cursor = connection.cursor()
#         query = "SELECT COUNT(corp_id) AS NumberOfCorporateCustomers FROM training_backend_corporate_customer"

#         cursor.execute(query)
#         r = cursor.fetchone()
#         print(r)
#         return JsonResponse(r, safe=False)


# @api_view(["PUT"])
# def corporate_fee_update(request):
#     cursor = connection.cursor()
#     customer_data = JSONParser().parse(request)
#     # customer_data = json.load(request)
#     print(customer_data)
#     query = "UPDATE training_backend_corporate_customer SET corp_total_fee=%s,corp_paid_fee=%s,corp_due_fee=%s,corp_units=%s WHERE corp_id=%s"

#     cursor.execute(
#         query,
#         params=(
#             customer_data["corp_total_fee"],
#             customer_data["corp_paid_fee"],
#             customer_data["corp_due_fee"],
#             customer_data["corp_units"],
#             customer_data["corp_id"],
#         ),
#     )
#     r = cursor.fetchone()
#     return JsonResponse(r, safe=False)


# # Sale


# @api_view(["GET", "POST"])
# def sale_list(request):
#     if request.method == "GET":
#         sale = Sale.objects.all()

#         # corp_name = request.GET.get("corp_name", None)
#         # if corp_name is not None:
#         #     sale = sale.filter(
#         #         corp_name__icontains=corp_name
#         #     )

#         sale_serializer = SaleSerializer(sale, many=True)
#         return JsonResponse(sale_serializer.data, safe=False)

#     elif request.method == "POST":
#         sale_data = JSONParser().parse(request)
#         sale_serializer = SaleSerializer(data=sale_data)
#         if sale_serializer.is_valid():
#             sale_serializer.save()
#             return JsonResponse(sale_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(sale_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def sale_detail(request, pk):
#     try:
#         sale = Sale.objects.get(pk=pk)
#     except Sale.DoesNotExist:
#         return JsonResponse(
#             {"message": "The sale record does not exist"},
#             status=status.HTTP_404_NOT_FOUND,
#         )

#     if request.method == "GET":
#         sale_serializer = SaleSerializer(sale)
#         return JsonResponse(sale_serializer.data)

#     elif request.method == "PUT":
#         sale_data = JSONParser().parse(request)
#         sale_serializer = SaleSerializer(data=sale_data)
#         if sale_serializer.is_valid():
#             sale_serializer.save()
#             return JsonResponse(sale_serializer.data)
#         return JsonResponse(sale_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         sale.delete()
#         return JsonResponse(
#             {"message": "sale record was deleted successfully!"},
#             status=status.HTTP_204_NO_CONTENT,
#         )


# @api_view(["GET"])
# def sale_count(request):
#     if request.method == "GET":
#         cursor = connection.cursor()
#         query = "SELECT COUNT(id) AS NumberOfSaleRecords FROM training_backend_sale"

#         cursor.execute(query)
#         r = cursor.fetchone()
#         print(r)
#         return JsonResponse(r, safe=False)


# @api_view(["GET"])
# def sale_id(request):
#     cursor = connection.cursor()
#     query = "SELECT id FROM training_backend_sale ORDER BY id DESC LIMIT 0,1"
#     cursor.execute(query)
#     r = cursor.fetchone()
#     print(r)
#     return JsonResponse(r, safe=False)


# params=(
#             customer_data["cust_total_fee"],
#             customer_data["cust_paid_fee"],
#             customer_data["cust_due_fee"],
#             customer_data["cust_id"],
#         ),


@api_view(["GET", "POST"])
def sale_report(request):
    if request.method == "GET":
        report = SaleReport.objects.all()

        report_serializer = SaleReportSerializer(report, many=True)
        return JsonResponse(report_serializer.data, safe=False)

    elif request.method == "POST":
        report_data = JSONParser().parse(request)
        report_serializer = SaleReportSerializer(data=report_data)
        if report_serializer.is_valid():
            report_serializer.save()
            return JsonResponse(report_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            report_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def sale_list(request):
    cursor = connection.cursor()
    query = "SELECT * FROM training_backend_salereport"

    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def sale_report_with_customers(request, batchId):
    cursor = connection.cursor()

    query1 = "SELECT *,(paid*inst_profit)/100 AS inst_fee,(paid*user_profit)/100 AS user_fee FROM training_backend_salereport INNER JOIN training_backend_customer ON training_backend_salereport.cust_id=training_backend_customer.cust_id"
    query2 = "SELECT *,(paid*inst_profit)/100 AS inst_fee,(paid*user_profit)/100 AS user_fee FROM training_backend_salereport INNER JOIN training_backend_customer ON training_backend_salereport.cust_id=training_backend_customer.cust_id WHERE batch_id=%s"

    if batchId == "None":
        cursor.execute(query1)
    else:
        cursor.execute(query2, params=(batchId))

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def sale_id(request):
    cursor = connection.cursor()
    query = "SELECT * FROM training_backend_salereport ORDER BY id DESC LIMIT 0,1"
    cursor.execute(query)
    r = cursor.fetchone()
    print(r)
    return JsonResponse(r, safe=False)


@api_view(["PUT"])
def sale_update(request):
    cursor = connection.cursor()
    customer_data = JSONParser().parse(request)
    # customer_data = json.load(request)
    print(customer_data)
    query = "UPDATE training_backend_salereport  SET installment2=%s,date2=%s,check_date2=%s,check_ref_no2=%s,pay_mode2=%s,installment3=%s,date3=%s,check_date3=%s,check_ref_no3=%s,pay_mode3=%s,installment4=%s,date4=%s,check_date4=%s,check_ref_no4=%s,pay_mode4=%s,paid=%s,due=%s WHERE id=%s"

    cursor.execute(
        query,
        params=(
            customer_data["installment2"],
            customer_data["date2"],
            customer_data["check_date2"],
            customer_data["check_ref_no2"],
            customer_data["pay_mode2"],
            customer_data["installment3"],
            customer_data["date3"],
            customer_data["check_date3"],
            customer_data["check_ref_no3"],
            customer_data["pay_mode3"],
            customer_data["installment4"],
            customer_data["date4"],
            customer_data["check_date4"],
            customer_data["check_ref_no4"],
            customer_data["pay_mode4"],
            customer_data["paid"],
            customer_data["due"],
            customer_data["id"],
        ),
    )
    r = cursor.fetchone()
    return JsonResponse(r, safe=False)
