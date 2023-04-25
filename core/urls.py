from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('upload/',UploadView.as_view(), name='upload'),
    path('screenshot/',upload_reception, name='screenshot'),


]

