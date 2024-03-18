from django.urls import path, include
from . import views


urlpatterns = [
    path('create_reminder/', views.create_reminder_message, name='create_reminder')
]