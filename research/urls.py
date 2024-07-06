from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('privacy-assessment/', views.privacy_assessment, name='privacy_assessment'),
    path('regulatory-evaluation/', views.regulatory_evaluation, name='regulatory_evaluation'),
    path('evaluation/', views.evaluation, name='evaluation'),
]

