from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from .models import RentalCarInfo
from .serializers import RentalCarSerializer


@csrf_exempt
def RentalCar_list(request):
    if request.method == 'GET':
        RentalCars = RentalCarInfo.objects.all()
        serializer = RentalCarSerializer(RentalCars, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RentalCarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def RentalCar_detail(request, pk):
    try:
        RentalCar = RentalCarInfo.objects.get(pk=pk)
    except RentalCarInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RentalCarSerializer(RentalCar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RentalCarSerializer(RentalCar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        RentalCar.delete()
        return HttpResponse(status=204)

