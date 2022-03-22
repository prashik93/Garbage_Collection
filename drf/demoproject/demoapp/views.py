from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Flat,Manager,Analytics
from .serializers import FlatSerializers,FlatManagerSerializers,AnalyticsSerializers

# Create your views here.
def home_view(request):
    return HttpResponse("HELLO WORLD")

class FlatOwner(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializers

class FlatManager(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = FlatManagerSerializers

class AnalyticsView(viewsets.ModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializers



