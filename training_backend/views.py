from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.relations import ManyRelatedField

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
