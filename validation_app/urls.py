# validation_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('participant_form/', views.participant_form, name='participant_form'),
    path('submission_success/', views.submission_success, name='submission_success'),
]
