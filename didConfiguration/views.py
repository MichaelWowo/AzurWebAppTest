from django.shortcuts import render
from didConfiguration.models import DidConfiguration
from didConfiguration.serializers import DidConfigurationSerializer
from rest_framework import viewsets

class DidConfigurationViewSet(viewsets.ModelViewSet):
    queryset = DidConfiguration.objects.all()
    serializer_class = DidConfigurationSerializer
    
