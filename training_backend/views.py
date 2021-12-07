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
    Retail_Customer,
    Corporate_Customer,
    Category,
    Course,
    Batch,
)
from training_backend.serializers import (
    InstructorSerializer,
    UserSerializer,
    RetailCustomerSerializer,
    CorporateCustomerSerializer,
    CategorySerializer,
    CourseSerializer,
    BatchSerializer,
    # NumberSerializer,
)
from rest_framework.decorators import api_view

# Create your views here.


# Instructor


@api_view(["GET", "POST"])
def instructor_list(request):
    if request.method == "GET":
        instructors = Instructor.objects.all()

        name = request.GET.get("name", None)
        if name is not None:
            instructors = instructors.filter(name__icontains=name)

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

        name = request.GET.get("name", None)
        if name is not None:
            users = users.filter(name__icontains=name)

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

        batch = request.GET.get("batch", None)
        if batch is not None:
            batches = batches.filter(batch__icontains=batch)

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


# Retail Customer


@api_view(["GET", "POST"])
def retail_customer_list(request):
    if request.method == "GET":
        retail_customers = Retail_Customer.objects.all()

        phone = request.GET.get("phone", None)
        if phone is not None:
            retail_customers = retail_customers.filter(phone__icontains=phone)

        retail_customers_serializer = RetailCustomerSerializer(
            retail_customers, many=True
        )
        return JsonResponse(retail_customers_serializer.data, safe=False)

    elif request.method == "POST":
        retail_customer_data = JSONParser().parse(request)
        retail_customers_serializer = RetailCustomerSerializer(
            data=retail_customer_data
        )
        if retail_customers_serializer.is_valid():
            retail_customers_serializer.save()
            return JsonResponse(
                retail_customers_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            retail_customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def retail_customer_detail(request, pk):
    try:
        retail_customer = Retail_Customer.objects.get(pk=pk)
    except Retail_Customer.DoesNotExist:
        return JsonResponse(
            {"message": "The retail_customer does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        retail_customer_serializer = RetailCustomerSerializer(retail_customer)
        return JsonResponse(retail_customer_serializer.data)

    elif request.method == "PUT":
        retail_customer_data = JSONParser().parse(request)
        retail_customers_serializer = RetailCustomerSerializer(
            data=retail_customer_data
        )
        if retail_customers_serializer.is_valid():
            retail_customers_serializer.save()
            return JsonResponse(retail_customers_serializer.data)
        return JsonResponse(
            retail_customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        retail_customer.delete()
        return JsonResponse(
            {"message": "retail_customer was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def retail_customer_count(request):
    if request.method == "GET":
        cursor = connection.cursor()
        query = "SELECT COUNT(cust_id) AS NumberOfRetailCustomers FROM training_backend_retail_customer"

        cursor.execute(query)
        r = cursor.fetchone()
        print(r)
        return JsonResponse(r, safe=False)


# Corporate customer


@api_view(["GET", "POST"])
def corporate_customer_list(request):
    if request.method == "GET":
        corporate_customers = Corporate_Customer.objects.all()

        name = request.GET.get("name", None)
        if name is not None:
            corporate_customers = corporate_customers.filter(name__icontains=name)

        corporate_customers_serializer = CorporateCustomerSerializer(
            corporate_customers, many=True
        )
        return JsonResponse(corporate_customers_serializer.data, safe=False)

    elif request.method == "POST":
        corporate_customer_data = JSONParser().parse(request)
        corporate_customers_serializer = CorporateCustomerSerializer(
            data=corporate_customer_data
        )
        if corporate_customers_serializer.is_valid():
            corporate_customers_serializer.save()
            return JsonResponse(
                corporate_customers_serializer.data, status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            corporate_customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def corporate_customer_detail(request, pk):
    try:
        corporate_customer = Corporate_Customer.objects.get(pk=pk)
    except Corporate_Customer.DoesNotExist:
        return JsonResponse(
            {"message": "The corporate_customer does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        corporate_customer_serializer = CorporateCustomerSerializer(corporate_customer)
        return JsonResponse(corporate_customer_serializer.data)

    elif request.method == "PUT":
        corporate_customer_data = JSONParser().parse(request)
        corporate_customers_serializer = CorporateCustomerSerializer(
            data=corporate_customer_data
        )
        if corporate_customers_serializer.is_valid():
            corporate_customers_serializer.save()
            return JsonResponse(corporate_customers_serializer.data)
        return JsonResponse(
            corporate_customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        corporate_customer.delete()
        return JsonResponse(
            {"message": "corporate_customer was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def corporate_customer_count(request):
    if request.method == "GET":
        cursor = connection.cursor()
        query = "SELECT COUNT(corp_id) AS NumberOfCorporateCustomers FROM training_backend_corporate_customer"

        cursor.execute(query)
        r = cursor.fetchone()
        print(r)
        return JsonResponse(r, safe=False)
