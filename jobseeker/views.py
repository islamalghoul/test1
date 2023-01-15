from django.shortcuts import render
from account.models import JobSeeker,ClientDetails,UserMedia
from rest_framework.generics import ListCreateAPIView
from .serializer import MediaSerializer,ClientDetailsSerializer,JobSeekerSerializer
from .permissions import Jobseeker
# Create your views here.
class JobseekerView(ListCreateAPIView):
    queryset=JobSeeker.objects.all()
    serializer_class=JobSeekerSerializer
    permission_classes=[Jobseeker]