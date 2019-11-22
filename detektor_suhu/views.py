from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from detektor_suhu.models import Stats
from detektor_suhu.serializers import StatsSerializer


class StatsViewSet(viewsets.ModelViewSet):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer

