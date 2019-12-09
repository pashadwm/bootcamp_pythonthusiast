from django.shortcuts import render
from rest_framework import viewsets
from upwork.models import Job
from upwork.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer