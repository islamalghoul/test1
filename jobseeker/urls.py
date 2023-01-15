from django.urls import path
from .views import JobseekerView
urlpatterns = [
    path('jobseeker/', JobseekerView.as_view()),
    
]   