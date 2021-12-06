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
    NumberSerializer,
)
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET", "POST"])
def instructor_list(request):
    if request.method == "GET":
        instructors = Instructor.objects.all()

        inst_name = request.GET.get("name", None)
        if inst_name is not None:
            instructors = instructors.filter(inst_name_icontains=inst_name)

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

    elif request.method == "DELETE":
        instructor.delete()
        return JsonResponse(
            {"message": "Tutorial was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET"])
def instructor_count(request):
    if request.method == "GET":
        number_of_instructors = Instructor.objects.raw(
            "SELECT COUNT(inst_id) AS NumberOfInstructors FROM training_backend_instructor"
        )
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
        r = cursor.fetchall()
        print(r)
        return JsonResponse(r, safe=False)


# objectQuerySet = ConventionCard.objects.filter(ownerUser = user)
# data = serializers.serialize('json', list(objectQuerySet), fields=('fileName','id'))
