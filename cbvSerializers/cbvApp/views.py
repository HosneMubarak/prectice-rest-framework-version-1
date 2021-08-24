from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class StudentPageNumber(PageNumberPagination):
    page_size = 2

#using ViewSet
class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPageNumber

#using generic api view

# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
# class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# using mixins
#
# class StudentList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class StudentDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)

# class StudentList(APIView):
#     def get(self, request):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class StudentDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
