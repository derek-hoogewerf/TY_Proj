from django.urls import path
from .views import FeedbackCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', FeedbackCreateView.as_view(), name='feedback'),
    
]