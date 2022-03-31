from django.urls import path
# from . import views
from . import views

app_name = "carClimate"

urlpatterns = [
    path('info/', views.InfoView.as_view(), name='info'),
    path('questions/', views.QuestionView.as_view(), name='questions'),
]