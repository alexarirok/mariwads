from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.dash_index, name='dash_index'),
    path('file_upload', views.file_upload, name='file_upload'),
    # path('model_form_upload', views.model_form_upload, name='model_form_upload'),
]