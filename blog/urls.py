from django.urls import path
from .views import post_list

urlpatterns = [
    # path('', index),
    path('list', post_list)
]