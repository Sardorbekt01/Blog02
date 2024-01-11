from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Branch,Employee,Car
from .serializers import BranchSerializer,EmployeeSerializer,CarSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# @api_view(["GET", ])
# def customfilter(request):
#     filterpost = Data.objects.filter(name__contains="S").filter(name__contains="1")
#     serialiser = DataSerializer(filterpost, many=True)
#     return Response(serialiser.data)

# # like "S"
# # like "1"
# # 
# # like

# @api_view(('GET', "POST"))
# def post(request):
#     if request.method == "GET":
#         post = Data.objects.all()
#         serializer = DataSerializer(post, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         post = DataSerializer(data=request.data)
#         if post.is_valid():
#             post.save()
#             return Response(post.data)


# @api_view(('GET', "DELETE", "PUT"))
# def postdetail(request, pk):
#     if request.method == "GET":
#         post = get_object_or_404(Data, id=pk)
#         serializer = DataSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         post = get_object_or_404(Data, id=pk)
#         serializer = DataSerializer(post, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         post = get_object_or_404(Data, id=pk)
#         post.delete()
#         return Response(status=204)
@api_view(('GET', "POST","DEL"))
def branch(request,pk,*args, **kwargs):
    if request.method == "GET":
        post = get_object_or_404(Branch, id=pk)
        serializer = BranchSerializer(post)
        return Response(serializer.data)
    elif request.method == "POST":
        post = BranchSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data)
    elif request.method == "DEL":
        post = get_object_or_404(Branch, id=pk)
        post.delete()
        return Response(status=204)
        
@api_view(('GET',"POST","DEL"))
def employee(request, pk):
    if request.method == "GET":
        post = get_object_or_404(Employee, id=pk)
        serializer = Employee(post)
        return Response(serializer.data)
    elif request.method == "POST":
        post = EmployeeSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data)
    elif request.method == "DEL":
        post = get_object_or_404(Employee, id=pk)
        post.delete()
        return Response(status=204)

@api_view(('GET', "DEL", "PUT"))
def cars(request, pk):
    if request.method == "GET":
        post = get_object_or_404(Car, id=pk)
        serializer = CarSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        post = get_object_or_404(Car, id=pk)
        serializer = CarSerializer(post, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == "DEL":
        post = get_object_or_404(Car, id=pk)
        post.delete()
        return Response(status=204)
