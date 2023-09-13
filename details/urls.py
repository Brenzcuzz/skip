from django.urls import path
from .views import index, save_data

urlpatterns = [
    path('',index, name='index' ),
    path('error404',save_data, name='save_data')
]
