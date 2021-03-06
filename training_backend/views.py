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
    InstructorFeeReport,
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
    InstructorFeeReportSerializer,
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


@api_view(["GET"])
def instructor_percentage(request, batchId):
    cursor = connection.cursor()

    query1 = "SELECT training_backend_salereport.inst_id,inst_name,training_backend_instructor.inst_profit,sum((paid*training_backend_salereport.inst_profit)/100) AS inst_fee FROM training_backend_salereport INNER JOIN training_backend_instructor ON training_backend_salereport.inst_id=training_backend_instructor.inst_id GROUP BY training_backend_salereport.inst_id"
    query2 = "SELECT training_backend_salereport.inst_id,inst_name,training_backend_instructor.inst_profit,sum((paid*training_backend_salereport.inst_profit)/100) AS inst_fee FROM training_backend_salereport INNER JOIN training_backend_instructor ON training_backend_salereport.inst_id=training_backend_instructor.inst_id WHERE batch_id=%s GROUP BY training_backend_salereport.inst_id"

    if batchId == "None":
        cursor.execute(query1)
    else:
        cursor.execute(query2, params=(batchId))

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def instructor_total(request, inst_id):
    cursor = connection.cursor()

    query = "SELECT inst_name,inst_payable,inst_paid,inst_due FROM training_backend_instructor WHERE inst_id=%s"

    cursor.execute(query, params=(inst_id))

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["PUT"])
def instructor_fee_update(request):
    cursor = connection.cursor()
    instructor_data = JSONParser().parse(request)
    print(instructor_data)
    query = "UPDATE training_backend_instructor SET inst_payable=%s,inst_paid=%s,inst_due=%s WHERE inst_id=%s"

    cursor.execute(
        query,
        params=(
            instructor_data["inst_payable"],
            instructor_data["inst_paid"],
            instructor_data["inst_due"],
            instructor_data["inst_id"],
        ),
    )
    r = cursor.fetchone()
    return JsonResponse(r, safe=False)


@api_view(["GET"])
def instructor_ledger(request):
    cursor = connection.cursor()

    query = "SELECT training_backend_instructor.inst_id,inst_name,inst_phone,training_backend_instructor.inst_profit,sum(batch_fee) AS sale,inst_payable,inst_paid,inst_due FROM training_backend_instructor INNER JOIN training_backend_salereport ON training_backend_instructor.inst_id=training_backend_salereport.inst_id GROUP BY training_backend_instructor.inst_id"
    cursor.execute(query)

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def batch_sale_payable(request, instId):
    cursor = connection.cursor()

    query = "SELECT batch_id,sum(batch_fee) as sale,sum((paid*inst_profit)/100) as payable FROM training_backend_salereport WHERE inst_id=%s GROUP BY batch_id"
    cursor.execute(query, params=(instId))

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def batch_paid_due(request, instId):
    cursor = connection.cursor()

    query = "SELECT training_backend_salereport.batch_id,sum(training_backend_instructorfeereport.paid) AS paid,min(training_backend_instructorfeereport.due) as due FROM training_backend_salereport LEFT OUTER JOIN training_backend_instructorfeereport ON training_backend_salereport.batch_id=training_backend_instructorfeereport.batch_id WHERE training_backend_salereport.inst_id=%s GROUP BY training_backend_salereport.batch_id"
    cursor.execute(query, params=(instId))

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


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


@api_view(["GET"])
def user_percentage(request, batchId):
    cursor = connection.cursor()

    query1 = "SELECT training_backend_salereport.user_id,user_name,training_backend_user.user_profit,sum((paid*training_backend_salereport.user_profit)/100) AS user_fee FROM training_backend_salereport INNER JOIN training_backend_user ON training_backend_salereport.user_id=training_backend_user.user_id GROUP BY training_backend_salereport.user_id"
    query2 = "SELECT training_backend_salereport.user_id,user_name,training_backend_user.user_profit,sum((paid*training_backend_salereport.user_profit)/100) AS user_fee FROM training_backend_salereport INNER JOIN training_backend_user ON training_backend_salereport.user_id=training_backend_user.user_id WHERE batch_id=%s GROUP BY training_backend_salereport.user_id"

    if batchId == "None":
        cursor.execute(query1)
    else:
        cursor.execute(query2, params=(batchId))

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


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
def batch_by_course(request, courseId):
    # batches = Batch.objects.all()
    # course_id = request.GET.get("course_id", None)
    cursor = connection.cursor()
    query = "SELECT batch_id,batch_num,batch_fee,inst_id,inst_profit from training_backend_batch WHERE course_id=%s"

    cursor.execute(query, params=courseId)
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def batch_ids(request):
    cursor = connection.cursor()
    query = "SELECT batch_id,training_backend_batch.course_id,batch_num,course_name FROM training_backend_batch INNER JOIN training_backend_course ON training_backend_batch.course_id=training_backend_course.course_id"

    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def batch_list_table(request):
    cursor = connection.cursor()
    query = "SELECT training_backend_batch.batch_id,training_backend_batch.batch_num,training_backend_batch.batch_fee,training_backend_batch.admit_closed,training_backend_course.course_name,training_backend_instructor.inst_name FROM training_backend_batch INNER JOIN training_backend_course ON training_backend_batch.course_id=training_backend_course.course_id INNER JOIN training_backend_instructor ON training_backend_batch.inst_id=training_backend_instructor.inst_id"

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


@api_view(["GET"])
def batches_by_instructor(request, instId):
    cursor = connection.cursor()
    query = "SELECT batch_id FROM training_backend_batch WHERE inst_id=%s"

    cursor.execute(query, params=(instId))
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


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


@api_view(["GET"])
def sale_total_payable(request, batchId):
    cursor = connection.cursor()
    query = "SELECT inst_id,sum(paid) AS pay_received,sum((paid*inst_profit)/100) AS inst_payable,sum(batch_fee) AS total_sale FROM training_backend_salereport WHERE batch_id=%s GROUP BY inst_id"

    cursor.execute(query, params=(batchId))
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def sale_report_with_customer_batch(request, custId):
    cursor = connection.cursor()
    query = "select training_backend_salereport.id,regular_fee,training_backend_salereport.batch_fee,installment1,mr_no1,date1,check_date1,check_ref_no1,pay_mode1,installment2,mr_no2,date2,check_date2,check_ref_no2,pay_mode2,installment3,mr_no3,date3,check_date3,check_ref_no3,pay_mode3,installment4,mr_no4,date4,check_date4,check_ref_no4,pay_mode4,paid,due,training_backend_salereport.inst_profit,training_backend_salereport.user_profit,remarks,training_backend_salereport.batch_id,training_backend_salereport.course_id,cust_id,training_backend_salereport.inst_id,training_backend_salereport.user_id,training_backend_batch.batch_num,training_backend_course.course_name from training_backend_salereport inner join training_backend_batch on training_backend_salereport.batch_id=training_backend_batch.batch_id inner join training_backend_course on training_backend_salereport.course_id=training_backend_course.course_id where cust_id=%s"

    cursor.execute(query, params=(custId))
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def sale_report_with_batch(request, batchId):
    cursor = connection.cursor()

    query1 = "select training_backend_salereport.id,regular_fee,training_backend_salereport.batch_fee,installment1,mr_no1,date1,check_date1,check_ref_no1,pay_mode1,installment2,mr_no2,date2,check_date2,check_ref_no2,pay_mode2,installment3,mr_no3,date3,check_date3,check_ref_no3,pay_mode3,installment4,mr_no4,date4,check_date4,check_ref_no4,pay_mode4,paid,due,training_backend_salereport.inst_profit,training_backend_salereport.user_profit,remarks,training_backend_salereport.batch_id,training_backend_salereport.course_id,training_backend_salereport.cust_id,training_backend_salereport.inst_id,training_backend_salereport.user_id,training_backend_batch.batch_num,training_backend_course.course_name,cust_name,cust_address,cust_email,cust_phone,cust_organization,cust_designation,(paid*training_backend_salereport.inst_profit)/100 AS inst_fee,(paid*training_backend_salereport.user_profit)/100 AS user_fee from training_backend_salereport inner join training_backend_batch on training_backend_salereport.batch_id=training_backend_batch.batch_id inner join training_backend_course on training_backend_salereport.course_id=training_backend_course.course_id inner join training_backend_customer on training_backend_salereport.cust_id=training_backend_customer.cust_id"
    query2 = "select training_backend_salereport.id,regular_fee,training_backend_salereport.batch_fee,installment1,mr_no1,date1,check_date1,check_ref_no1,pay_mode1,installment2,mr_no2,date2,check_date2,check_ref_no2,pay_mode2,installment3,mr_no3,date3,check_date3,check_ref_no3,pay_mode3,installment4,mr_no4,date4,check_date4,check_ref_no4,pay_mode4,paid,due,training_backend_salereport.inst_profit,training_backend_salereport.user_profit,remarks,training_backend_salereport.batch_id,training_backend_salereport.course_id,training_backend_salereport.cust_id,training_backend_salereport.inst_id,training_backend_salereport.user_id,training_backend_batch.batch_num,training_backend_course.course_name,cust_name,cust_address,cust_email,cust_phone,cust_organization,cust_designation,(paid*training_backend_salereport.inst_profit)/100 AS inst_fee,(paid*training_backend_salereport.user_profit)/100 AS user_fee from training_backend_salereport inner join training_backend_batch on training_backend_salereport.batch_id=training_backend_batch.batch_id inner join training_backend_course on training_backend_salereport.course_id=training_backend_course.course_id inner join training_backend_customer on training_backend_salereport.cust_id=training_backend_customer.cust_id where training_backend_salereport.batch_id=%s"
    if batchId == "None":
        cursor.execute(query1)
    else:
        cursor.execute(query2, params=(batchId))

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


# Instructor Fee Report


@api_view(["GET"])
def inst_paid_due(request, batchId):
    cursor = connection.cursor()
    query = "SELECT sum(paid) AS paid,MIN(due) as due FROM training_backend_instructorfeereport WHERE batch_id=%s"

    cursor.execute(query, params=(batchId))
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET", "POST"])
def instructor_fee_report(request):
    if request.method == "GET":
        report = InstructorFeeReport.objects.all()

        report_serializer = InstructorFeeReportSerializer(report, many=True)
        return JsonResponse(report_serializer.data, safe=False)

    elif request.method == "POST":
        report_data = JSONParser().parse(request)
        report_serializer = InstructorFeeReportSerializer(data=report_data)
        if report_serializer.is_valid():
            report_serializer.save()
            return JsonResponse(report_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            report_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def instructor_fee_by_batch(request, batchId):
    cursor = connection.cursor()
    query = "SELECT * FROM training_backend_instructorfeereport WHERE batch_id=%s"

    cursor.execute(query, params=(batchId))
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )
