from django.contrib import admin
from django.urls import path

from blog.views import posts_list

urlpatterns = [
    path('', posts_list),
]
